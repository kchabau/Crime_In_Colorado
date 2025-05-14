-- test
SELECT *
FROM crimes_in_colorado
LIMIT 15;

-- total amount of records imported 
SELECT COUNT(*)
FROM crimes_in_colorado;


-- min and max age 
SELECT 
    MAX(age_num_imputed),
    MIN(age_num_imputed)
FROM crimes_in_colorado;

-- the percentage and number of total incidents that came from particular age group 
SELECT
    CASE
        WHEN age_num_imputed <= 15 THEN 'Adolescent'
        WHEN age_num_imputed BETWEEN 16 AND 24 THEN 'Young Adult'
        WHEN age_num_imputed BETWEEN 25 AND 39 THEN 'Middle Age Adult'
        WHEN age_num_imputed BETWEEN 40 AND 59 THEN 'Adult'
        ELSE 'Senior'
    END AS age_group,
    COUNT(*) AS count_in_group,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS percent_of_total
FROM crimes_in_colorado
GROUP BY age_group
ORDER BY percent_of_total DESC;


-- the percentage of total incidents in the county that came from particular age group.
WITH age_cat AS (
    SELECT 
        county_name,
        CASE
            WHEN age_num_imputed <= 15 THEN 'Adolescent'
            WHEN age_num_imputed BETWEEN 16 AND 24 THEN 'Young Adult'
            WHEN age_num_imputed BETWEEN 25 AND 39 THEN 'Middle Age Adult'
            WHEN age_num_imputed BETWEEN 40 AND 59 THEN 'Adult'
            ELSE 'Senior'
        END AS age_group
    FROM crimes_in_colorado
)
SELECT
    county_name,
    age_group,
    COUNT(*) AS `count`,
    ROUND(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY county_name),2
    ) AS `% of Incident Reports (per age_group and county_name)`
FROM age_cat
GROUP BY county_name, age_group
ORDER BY  COUNT(*) DESC, 4 DESC;



-- Reports of incidents occurring in the state of Colorado (by offense_name)
SELECT
    offense_name,
    COUNT(*) AS number_of_offenses_reported
FROM crimes_in_colorado
GROUP BY offense_name
ORDER BY COUNT(*) DESC;
-- the percentage of total incidents in the offense_name that came from particular age group.
WITH age_cat AS (
    SELECT 
        offense_name,
        CASE
            WHEN age_num_imputed <= 15 THEN 'Adolescent'
            WHEN age_num_imputed BETWEEN 16 AND 24 THEN 'Young Adult'
            WHEN age_num_imputed BETWEEN 25 AND 39 THEN 'Middle Age Adult'
            WHEN age_num_imputed BETWEEN 40 AND 59 THEN 'Adult'
            ELSE 'Senior'
        END AS age_group
    FROM crimes_in_colorado
)
SELECT
    offense_name,
    age_group,
    COUNT(*) AS `count`,
    ROUND(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY offense_name),2
    ) AS `% of Incident Reports (per age_group and offense_name)`
FROM age_cat
GROUP BY offense_name, age_group
ORDER BY  COUNT(*) DESC, 4 DESC;


-- number of offenses reported throughout the years 
SELECT 
    YEAR(incident_date_converted) AS year,
    COUNT(*) AS num_of_reports
FROM crimes_in_colorado
GROUP BY YEAR(incident_date_converted)
ORDER BY YEAR(incident_date_converted) ASC;

-- number of offenses reported throughout the years (per category name)
SELECT *
FROM (
    SELECT 
        YEAR(incident_date_converted) AS year,
        offense_category_name,
        COUNT(*) AS num_of_reports,
        RANK() OVER(PARTITION BY YEAR(incident_date_converted) ORDER BY COUNT(*) DESC) AS ranking
    FROM crimes_in_colorado
    GROUP BY YEAR(incident_date_converted), offense_category_name
) AS ranked_crimes
WHERE ranking BETWEEN 1 AND 5
ORDER BY year ASC, ranking ASC;


-- Rank most dangerous cities (by the number of reported crimes)
WITH cities_ranked AS(
    SELECT 
        pub_agency_name,
        COUNT(*) AS num_of_reports,
        RANK() OVER(ORDER BY COUNT(*) DESC) AS ranking
    FROM crimes_in_colorado
    GROUP BY pub_agency_name
)
SELECT 
    ranking,
    pub_agency_name,
    num_of_reports
FROM cities_ranked
WHERE ranking BETWEEN 1 and 50
ORDER BY ranking ASC;


-- Running average of Crimes in each City throughout the year and month
SELECT 
    year,
    crime_count,
    SUM(crime_count) OVER (ORDER BY year) AS running_total,
    AVG(crime_count) OVER (ORDER BY year) AS running_avg,
    COUNT(*) OVER (ORDER BY year) AS running_count
FROM (
    SELECT 
        YEAR(incident_date_converted) AS year,
        COUNT(*) AS crime_count
    FROM crimes_in_colorado
    GROUP BY YEAR(incident_date_converted)
) AS yearly_data;

-- Develop a 2D Heatmap showing the frequency of offense categories in each pub_agency_name 
-- Complete using Python 
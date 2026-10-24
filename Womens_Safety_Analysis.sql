USE womens_safety_db;
SELECT * FROM womens_safety_data LIMIT 5;
SELECT
    'CRIME HEAD',
      SUM('2001' + '2002' + '2003' + '2004' + '2005' + '2006' + '2007' + '2008' + '2009' + '2010' + '2011' + '2012') AS total_crimes
     FROM womens_safety_data
     GROUP BY 'CRIME HEAD'
     ORDER BY total_crimes DESC;
SELECT COUNT(DISTINCT 'CRIME HEAD') AS total_categories FROM womens_safety_data;
SELECT * FROM womens_safety_data LIMIT 10;
SELECT COUNT(*) AS total_rows FROM womens_safety_data;
SELECT DISTINCT 'STATE/UT' FROM womens_safety_data;
SELECT DISTINCT state_ut FROM womens_safety_data;
SELECT DISTINCT crime_head FROM womens_safety_data;
SELECT
    crime_head,
    SUM(
        year_2001 + year_2002 + year_2003 + year_2004 + year_2005 + year_2005 + year_2007 + year_2008 + year_2009 + year_2010 + year_2011 + year_2012)
        AS TOTAL_CRIMES
        FROM womens_safety_data
        GROUP BY crime_head
        ORDER BY total_crimes DESC;
SELECT
    SUM(year_2001) AS total_2001,
    SUM(year_2002) AS total_2002,
    SUM(year_2003) AS total_2003,
    SUM(YEAR_2004) AS total_2004,
    SUM(year_2005) AS total_2005,
    SUM(year_2006) AS total_2006,
    SUM(year_2007) AS total_2007,
    SUM(year_2008) AS total_2008,
    SUM(year_2009) AS total_2009,
    SUM(year_2010) AS total_2010,
    SUM(year_2011) AS total_2011,
    SUM(year_2012) AS total_2012
 FROM womens_safety_data 
 WHERE crime_head = 'TOTAL CRIMES AGAINST WOMEN';
 SELECT 
      state_ut,
      SUM(year_2001 + year_2002 + year_2003 + year_2004 + year_2005 + year_2006 + year_2007 + year_2008 + year_2009 + year_2010 + year_2011 + year_2012)
      AS total_crimes FROM womens_safety_data
      WHERE crime_head = ' TOTAL CRIMES AGAINST WOMEN'
      GROUP BY state_ut ORDER BY total_crimes DESC;
SELECT DISTINCT crime_head
FROM womens_safety_data;

SELECT DISTINCT crime_head
FROM womens_safety_data
WHERE crime_head LIKE '%TOTAL%';
SELECT
    state_ut,
    SUM(
        year_2001 + year_2002 + year_2003 + year_2004 +
        year_2005 + year_2006 + year_2007 + year_2008 +
        year_2009 + year_2010
        + year_2011 + year_2012
    ) AS total_crimes
FROM womens_safety_data
WHERE LOWER(crime_head) = 'total crimes against women'
GROUP BY state_ut
ORDER BY total_crimes DESC;
USE womens_safety_db;

SELECT
    state_ut,
    SUM(
        year_2001 + year_2002 + year_2003 + year_2004 +
        year_2005 + year_2006 + year_2007 + year_2008 +
        year_2009 + year_2010 + year_2011 + year_2012
    ) AS total_crimes
FROM womens_safety_data
WHERE LOWER(crime_head) = 'total crimes against women'
GROUP BY state_ut
ORDER BY total_crimes DESC
LIMIT 10;
SELECT
    SUM(year_2001) AS total_2001,
    SUM(year_2002) AS total_2002,
    SUM(year_2003) AS total_2003,
    SUM(year_2004) AS total_2004,
    SUM(year_2005) AS total_2005,
    SUM(year_2006) AS total_2006,
    SUM(year_2007) AS total_2007,
    SUM(year_2008) AS total_2008,
    SUM(year_2009) AS total_2009,
    SUM(year_2010) AS total_2010,
    SUM(year_2011) AS total_2011,
    SUM(year_2012) AS total_2012
FROM womens_safety_data
WHERE LOWER(crime_head) = 'total crimes against women';
SELECT
    crime_head,
    SUM(
        year_2001 + year_2002 + year_2003 +
        year_2004 + year_2005 + year_2006 +
        year_2007 + year_2008 + year_2009 +
        year_2010 + year_2011 + year_2012
    ) AS total_crimes
FROM womens_safety_data
WHERE LOWER(crime_head) != 'total crimes against women'
GROUP BY crime_head
ORDER BY total_crimes DESC;
SELECT
    state_ut,
    SUM(
        year_2001 + year_2002 + year_2003 +
        year_2004 + year_2005 + year_2006 +
        year_2007 + year_2008 + year_2009 +
        year_2010 + year_2011 + year_2012
    ) AS total_crimes
FROM womens_safety_data
WHERE LOWER(crime_head) = 'total crimes against women'
GROUP BY state_ut
ORDER BY total_crimes DESC;
SELECT
    crime_head,
    SUM(year_2001) AS total_2001,
    SUM(year_2002) AS total_2002,
    SUM(year_2003) AS total_2003,
    SUM(year_2004) AS total_2004,
    SUM(year_2005) AS total_2005,
    SUM(year_2006) AS total_2006,
    SUM(year_2007) AS total_2007,
    SUM(year_2008) AS total_2008,
    SUM(year_2009) AS total_2009,
    SUM(year_2010) AS total_2010,
    SUM(year_2011) AS total_2011,
    SUM(year_2012) AS total_2012
FROM womens_safety_data
WHERE LOWER(crime_head) != 'total crimes against women'
GROUP BY crime_head
ORDER BY crime_head;
SELECT
    crime_head,
    SUM(
        year_2001 + year_2002 + year_2003 +
        year_2004 + year_2005 + year_2006 +
        year_2007 + year_2008 + year_2009 +
        year_2010 + year_2011 + year_2012
    ) AS total_crimes
FROM womens_safety_data
WHERE LOWER(crime_head) != 'total crimes against women'
GROUP BY crime_head
ORDER BY total_crimes DESC
LIMIT 5;
SELECT
    crime_head,
    SUM(
        year_2001 + year_2002 + year_2003 +
        year_2004 + year_2005 + year_2006 +
        year_2007 + year_2008 + year_2009 +
        year_2010 + year_2011 + year_2012
    ) AS total_crimes,
    ROUND(
        SUM(
            year_2001 + year_2002 + year_2003 +
            year_2004 + year_2005 + year_2006 +
            year_2007 + year_2008 + year_2009 +
            year_2010 + year_2011 + year_2012
        ) * 100.0 /
        (
            SELECT SUM(
                year_2001 + year_2002 + year_2003 +
                year_2004 + year_2005 + year_2006 +
                year_2007 + year_2008 + year_2009 +
                year_2010 + year_2011 + year_2012
            )
            FROM womens_safety_data
            WHERE LOWER(crime_head) != 'total crimes against women'
        ),
        2
    ) AS percentage_contribution
FROM womens_safety_data
WHERE LOWER(crime_head) != 'total crimes against women'
GROUP BY crime_head
ORDER BY percentage_contribution DESC;
WITH yearly_totals AS (
    SELECT
        SUM(year_2001) AS y2001,
        SUM(year_2002) AS y2002,
        SUM(year_2003) AS y2003,
        SUM(year_2004) AS y2004,
        SUM(year_2005) AS y2005,
        SUM(year_2006) AS y2006,
        SUM(year_2007) AS y2007,
        SUM(year_2008) AS y2008,
        SUM(year_2009) AS y2009,
        SUM(year_2010) AS y2010,
        SUM(year_2011) AS y2011,
        SUM(year_2012) AS y2012
    FROM womens_safety_data
    WHERE LOWER(crime_head) = 'total crimes against women'
),
yearly_rows AS (
    SELECT 2001 AS year, y2001 AS total_crimes FROM yearly_totals
    UNION ALL SELECT 2002, y2002 FROM yearly_totals
    UNION ALL SELECT 2003, y2003 FROM yearly_totals
    UNION ALL SELECT 2004, y2004 FROM yearly_totals
    UNION ALL SELECT 2005, y2005 FROM yearly_totals
    UNION ALL SELECT 2006, y2006 FROM yearly_totals
    UNION ALL SELECT 2007, y2007 FROM yearly_totals
    UNION ALL SELECT 2008, y2008 FROM yearly_totals
    UNION ALL SELECT 2009, y2009 FROM yearly_totals
    UNION ALL SELECT 2010, y2010 FROM yearly_totals
    UNION ALL SELECT 2011, y2011 FROM yearly_totals
    UNION ALL SELECT 2012, y2012 FROM yearly_totals
)
SELECT
    year,
    total_crimes,
    LAG(total_crimes) OVER (ORDER BY year) AS previous_year_crimes,
    ROUND(
        (total_crimes - LAG(total_crimes) OVER (ORDER BY year))
        * 100.0 /
        NULLIF(LAG(total_crimes) OVER (ORDER BY year), 0),
        2
    ) AS growth_percentage
FROM yearly_rows
ORDER BY year;
WITH yearly_totals AS (
    SELECT
        SUM(year_2001) AS y2001,
        SUM(year_2002) AS y2002,
        SUM(year_2003) AS y2003,
        SUM(year_2004) AS y2004,
        SUM(year_2005) AS y2005,
        SUM(year_2006) AS y2006,
        SUM(year_2007) AS y2007,
        SUM(year_2008) AS y2008,
        SUM(year_2009) AS y2009,
        SUM(year_2010) AS y2010,
        SUM(year_2011) AS y2011,
        SUM(year_2012) AS y2012
    FROM womens_safety_data
    WHERE LOWER(crime_head) = 'total crimes against women'
),
yearly_rows AS (
    SELECT 2001 AS year, y2001 AS total_crimes FROM yearly_totals
    UNION ALL SELECT 2002, y2002 FROM yearly_totals
    UNION ALL SELECT 2003, y2003 FROM yearly_totals
    UNION ALL SELECT 2004, y2004 FROM yearly_totals
    UNION ALL SELECT 2005, y2005 FROM yearly_totals
    UNION ALL SELECT 2006, y2006 FROM yearly_totals
    UNION ALL SELECT 2007, y2007 FROM yearly_totals
    UNION ALL SELECT 2008, y2008 FROM yearly_totals
    UNION ALL SELECT 2009, y2009 FROM yearly_totals
    UNION ALL SELECT 2010, y2010 FROM yearly_totals
    UNION ALL SELECT 2011, y2011 FROM yearly_totals
    UNION ALL SELECT 2012, y2012 FROM yearly_totals
),
growth_analysis AS (
    SELECT
        year,
        total_crimes,
        LAG(total_crimes) OVER (ORDER BY year) AS previous_year_crimes
    FROM yearly_rows
)
SELECT
    year,
    total_crimes,
    previous_year_crimes,
    ROUND(
        (total_crimes - previous_year_crimes) * 100.0 /
        NULLIF(previous_year_crimes, 0),
        2
    ) AS growth_percentage
FROM growth_analysis
WHERE previous_year_crimes IS NOT NULL
ORDER BY growth_percentage DESC
WITH yearly_totals AS (
    SELECT
        SUM(year_2001) AS y2001,
        SUM(year_2002) AS y2002,
        SUM(year_2003) AS y2003,
        SUM(year_2004) AS y2004,
        SUM(year_2005) AS y2005,
        SUM(year_2006) AS y2006,
        SUM(year_2007) AS y2007,
        SUM(year_2008) AS y2008,
        SUM(year_2009) AS y2009,
        SUM(year_2010) AS y2010,
        SUM(year_2011) AS y2011,
        SUM(year_2012) AS y2012
    FROM womens_safety_data
    WHERE LOWER(crime_head) = 'total crimes against women'
),
yearly_rows AS (
    SELECT 2001 AS year, y2001 AS total_crimes FROM yearly_totals
    UNION ALL SELECT 2002, y2002 FROM yearly_totals
    UNION ALL SELECT 2003, y2003 FROM yearly_totals
    UNION ALL SELECT 2004, y2004 FROM yearly_totals
    UNION ALL SELECT 2005, y2005 FROM yearly_totals
    UNION ALL SELECT 2006, y2006 FROM yearly_totals
    UNION ALL SELECT 2007, y2007 FROM yearly_totals
    UNION ALL SELECT 2008, y2008 FROM yearly_totals
    UNION ALL SELECT 2009, y2009 FROM yearly_totals
    UNION ALL SELECT 2010, y2010 FROM yearly_totals
    UNION ALL SELECT 2011, y2011 FROM yearly_totals
    UNION ALL SELECT 2012, y2012 FROM yearly_totals
),
growth_analysis AS (
    SELECT
        year,
        total_crimes,
        LAG(total_crimes) OVER (ORDER BY year) AS previous_year_crimes
    FROM yearly_rows
)
SELECT
    year,
    total_crimes,
    previous_year_crimes,
    ROUND(
        (total_crimes - previous_year_crimes) * 100.0 /
        NULLIF(previous_year_crimes, 0),
        2
    ) AS growth_percentage
FROM growth_analysis
WHERE previous_year_crimes IS NOT NULL
ORDER BY growth_percentage DESC
LIMIT 1;
WITH category_totals AS (
    SELECT
        state_ut,
        crime_head,
        SUM(
            year_2001 + year_2002 + year_2003 +
            year_2004 + year_2005 + year_2006 +
            year_2007 + year_2008 + year_2009 +
            year_2010 + year_2011 + year_2012
        ) AS total_crimes
    FROM womens_safety_data
    WHERE LOWER(crime_head) != 'total crimes against women'
    GROUP BY state_ut, crime_head
),
ranked_categories AS (
    SELECT
        state_ut,
        crime_head,
        total_crimes,
        RANK() OVER (
            PARTITION BY state_ut
            ORDER BY total_crimes DESC
        ) AS crime_rank
    FROM category_totals
)
SELECT
    state_ut,
    crime_head,
    total_crimes
FROM ranked_categories
WHERE crime_rank = 1
ORDER BY state_ut;
SELECT
    state_ut,
    SUM(
        year_2001 + year_2002 + year_2003 +
        year_2004 + year_2005 + year_2006 +
        year_2007 + year_2008 + year_2009 +
        year_2010 + year_2011 + year_2012
    ) AS total_crimes,
    ROUND(
        SUM(
            year_2001 + year_2002 + year_2003 +
            year_2004 + year_2005 + year_2006 +
            year_2007 + year_2008 + year_2009 +
            year_2010 + year_2011 + year_2012
        ) * 100.0 /
        (
            SELECT SUM(
                year_2001 + year_2002 + year_2003 +
                year_2004 + year_2005 + year_2006 +
                year_2007 + year_2008 + year_2009 +
                year_2010 + year_2011 + year_2012
            )
            FROM womens_safety_data
            WHERE LOWER(crime_head) = 'total crimes against women'
        ),
        2
    ) AS percentage_contribution
FROM womens_safety_data
WHERE LOWER(crime_head) = 'total crimes against women'
GROUP BY state_ut
ORDER BY percentage_contribution DESC;
SELECT
    state_ut,
    SUM(
        year_2001 + year_2002 + year_2003 +
        year_2004 + year_2005 + year_2006 +
        year_2007 + year_2008 + year_2009 +
        year_2010 + year_2011 + year_2012
    ) AS total_crimes
FROM womens_safety_data
WHERE LOWER(crime_head) = 'total crimes against women'
GROUP BY state_ut
ORDER BY total_crimes DESC
LIMIT 10;
SELECT
    crime_head,
    SUM(
        year_2001 + year_2002 + year_2003 +
        year_2004 + year_2005 + year_2006 +
        year_2007 + year_2008 + year_2009 +
        year_2010 + year_2011 + year_2012
    ) AS total_crimes,
    CASE
        WHEN SUM(
            year_2001 + year_2002 + year_2003 +
            year_2004 + year_2005 + year_2006 +
            year_2007 + year_2008 + year_2009 +
            year_2010 + year_2011 + year_2012
        ) >= 500000 THEN 'High'
        WHEN SUM(
            year_2001 + year_2002 + year_2003 +
            year_2004 + year_2005 + year_2006 +
            year_2007 + year_2008 + year_2009 +
            year_2010 + year_2011 + year_2012
        ) >= 100000 THEN 'Medium'
        ELSE 'Low'
    END AS crime_category_level
FROM womens_safety_data
WHERE LOWER(crime_head) != 'total crimes against women'
GROUP BY crime_head
ORDER BY total_crimes DESC;
SELECT
    SUM(year_2001) AS year_2001,
    SUM(year_2002) AS year_2002,
    SUM(year_2003) AS year_2003,
    SUM(year_2004) AS year_2004,
    SUM(year_2005) AS year_2005,
    SUM(year_2006) AS year_2006,
    SUM(year_2007) AS year_2007,
    SUM(year_2008) AS year_2008,
    SUM(year_2009) AS year_2009,
    SUM(year_2010) AS year_2010,
    SUM(year_2011) AS year_2011,
    SUM(year_2012) AS year_2012
FROM womens_safety_data
WHERE LOWER(crime_head) = 'total crimes against women';




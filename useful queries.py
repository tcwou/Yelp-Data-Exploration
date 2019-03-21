# Data Visualisation Project Dashboard
# 1) SQL database statistics, visualization of Relations and Tables
# 2) Yelp business KPIs Distribution of age of users, distribution of elite users
# 3) Distribution of businesses. # of reviews/ average rating per City
# 4) Detailed investigation into Las Vegas (most reviews)


# Get number of rows for each table
s = """ SELECT (SELECT COUNT(*) FROM business),
 (SELECT COUNT(*) FROM user),
 (SELECT COUNT(*) FROM review)"""
(192609, 1637138, 6685900)

# City, state, no of businesses, no of reviews,  of top 10 cities with most eateries
s = """ SELECT city, state, COUNT(DISTINCT(b.business_id)), COUNT(DISTINCT(review_id))
        FROM business b
        JOIN review r ON r.business_id = b.business_id
        JOIN category c ON c.business_id = b.business_id
        WHERE c.food = 1 
        GROUP BY city ORDER BY COUNT(b.business_id) DESC LIMIT 10 """
('Toronto', 'ON', 10071, 421871)
('Las Vegas', 'NV', 8266, 1334615)
('Phoenix', 'AZ', 5103, 460879)
('Montréal', 'QC', 4508, 129614)
('Charlotte', 'NC', 3480, 226922)
('Pittsburgh', 'PA', 3113, 177191)
('Scottsdale', 'AZ', 1992, 246043)
('Tempe', 'AZ', 1339, 128880)
('Henderson', 'NV', 1167, 125575)
('Cleveland', 'OH', 1799, 91805)

# Average stars of eateries in top 10 cities (subquery to prevent double counting stars after join)

s = """ SELECT city, state, COUNT(business_id), AVG(stars) 
        FROM
        (SELECT city, state, b.business_id, stars
        FROM business b
        JOIN category c ON c.business_id = b.business_id
        WHERE c.food = 1
        GROUP BY b.business_id) 
        GROUP BY city ORDER BY COUNT(business_id) DESC LIMIT 10 """

('Toronto', 'ON', 10071, 3.4658921656240693)
('Las Vegas', 'NV', 8266, 3.5046576336801354)
('Phoenix', 'AZ', 5103, 3.4846168920242993)
('Montréal', 'QC', 4508, 3.734028393966282)
('Calgary', 'AB', 3674, 3.5096624931954272)
('Charlotte', 'NC', 3480, 3.4632183908045975)
('Pittsburgh', 'PA', 3113, 3.5740443302280758)
('Scottsdale', 'AZ', 1992, 3.661144578313253)
('Cleveland', 'OH', 1799, 3.5405780989438576)
('Mississauga', 'ON', 1725, 3.3507246376811595)

# Categories of

# Get total open time for business on each day of the week
s = """ SELECT
AVG(CASE WHEN (strftime("%H", mon_close) - strftime("%H", mon_open)) <= 0 
THEN 24 + (strftime("%H", mon_close) - strftime("%H", mon_open)) 
ELSE (strftime("%H", mon_close) - strftime("%H", mon_open)) END),  

AVG(CASE WHEN (strftime("%H", tue_close) - strftime("%H", tue_open)) <= 0 
THEN 24 + (strftime("%H", tue_close) - strftime("%H", tue_open)) 
ELSE (strftime("%H", tue_close) - strftime("%H", tue_open)) END),  

AVG(CASE WHEN (strftime("%H", wed_close) - strftime("%H", wed_open)) <= 0 
THEN 24 + (strftime("%H", wed_close) - strftime("%H", wed_open)) 
ELSE (strftime("%H", wed_close) - strftime("%H", wed_open)) END),  

AVG(CASE WHEN (strftime("%H", thu_close) - strftime("%H", thu_open)) <= 0 
THEN 24 + (strftime("%H", thu_close) - strftime("%H", thu_open)) 
ELSE (strftime("%H", thu_close) - strftime("%H", thu_open)) END),  

AVG(CASE WHEN (strftime("%H", fri_close) - strftime("%H", fri_open)) <= 0 
THEN 24 + (strftime("%H", fri_close) - strftime("%H", fri_open)) 
ELSE (strftime("%H", fri_close) - strftime("%H", fri_open)) END),  

AVG(CASE WHEN (strftime("%H", sat_close) - strftime("%H", sat_open)) <= 0 
THEN 24 + (strftime("%H", sat_close) - strftime("%H", sat_open)) 
ELSE (strftime("%H", sat_close) - strftime("%H", sat_open)) END),  

AVG(CASE WHEN (strftime("%H", sun_close) - strftime("%H", sun_open)) <= 0 
THEN 24 + (strftime("%H", sun_close) - strftime("%H", sun_open)) 
ELSE (strftime("%H", sun_close) - strftime("%H", sun_open)) END)

FROM hours"""
(12.608255319775793, 11.123867027358674, 11.090350448135467, 11.15289610220489, 11.237156791160952, 10.908518127140258, 10.910396776736446)

# Average review length
s = """ SELECT AVG(LENGTH(text))
        FROM review """
(602.9766729983996,)

# Number of users, Average no of review, rating, review length grouped by number of year of elite
s = """ SELECT elite, COUNT(*), AVG(review_count), AVG(average_stars), AVG(LENGTH(text))
        FROM review JOIN user ON user.user_id = review.user_id GROUP BY elite """
(0, 5338376, 41.75646844658375, 3.707803633542564, 536.6499175030009)
(1, 327058, 171.6208134337029, 3.8784137064370694, 761.4445144286334)
(2, 279978, 251.51217952839153, 3.851132196100736, 816.6922079591968)
(3, 193766, 301.0434906020664, 3.8215747860822806, 863.226009723068)
(4, 135946, 437.6176496550101, 3.7929934679949167, 908.56328983567)
(5, 115937, 506.44940786806626, 3.7701892407082305, 952.8688598117943)
(6, 112149, 796.5037494761433, 3.7578857591240293, 1023.2671713523972)
(7, 68239, 705.6243057489119, 3.785366872316959, 918.9221559518751)
(8, 62607, 1202.2286006357117, 3.768117462903658, 966.8385963230949)
(9, 30944, 1733.6341455532574, 3.6930219105480857, 935.2119635470527)
(10, 12303, 1159.4819962610745, 3.723240673006574, 972.85979029505)
(11, 5729, 1605.5651946238436, 3.837495199860462, 983.906964566242)
(12, 2868, 1866.6258716875873, 3.7086506276150204, 1086.9926778242677)

# User sign up date per year and review count per uear
s1 = """ 
SELECT
strftime('%Y', yelping_since), COUNT(*)
FROM user GROUP BY strftime('%Y', yelping_since)
"""
s2 = """ 
SELECT
strftime('%Y', date), COUNT(*)
FROM review GROUP BY strftime('%Y', date)
"""
('2004', 81)
('2005', 1001)
('2006', 5836)
('2007', 16480)
('2008', 32544)
('2009', 63977)
('2010', 106840)
('2011', 168467)
('2012', 182900)
('2013', 197220)
('2014', 225437)
('2015', 238660)
('2016', 199148)
('2017', 120531)
('2018', 78016)

# Select all eateries in Las Vegas and combine all categories

s = """ 
SELECT b.business_id, name, latitude, longitude, stars, review_count, group_concat(category, ", ")
FROM business b
JOIN category c ON b.business_id = c.business_id
WHERE c.food = 1 AND city in ('Las Vegas', 'Henderson', 'North Las Vegas')
GROUP BY b.business_id
"""


# SELECT 30000 vegas eatery reviews, subquery

s = """ 
SELECT wr
FROM (SELECT b.business_id b_id, AVG(stars) b_stars, group_concat(category, ", ") cats
FROM business b
JOIN category c ON b.business_id = c.business_id
WHERE c.food = 1 AND city in ('Las Vegas', 'Henderson', 'North Las Vegas')
GROUP BY b.business_id)
JOIN review r ON r.business_id = b_id
LIMIT 30000
"""

# select yearly growth

s1 = """ 
WITH 
year_new_users as (
SELECT strftime('%Y', yelping_since) year, COUNT(*) new_users
FROM user GROUP BY 1
),
prev_year_new_users as (
SELECT *,
lag(new_users) OVER (ORDER BY year) AS prev_new_users
FROM year_new_users
),
year_new_reviews as (
SELECT strftime('%Y', date) year, COUNT(*) new_reviews
FROM review GROUP BY 1
),
prev_year_new_reviews as (
SELECT *,
lag(new_reviews) OVER (ORDER BY year) AS prev_new_reviews
FROM year_new_reviews
)

SELECT r.year, new_users, new_reviews,
round(100*(new_users-prev_new_users)/prev_new_users,1) as user_growth,
round(100*(new_reviews-prev_new_reviews)/prev_new_reviews,1) as review_growth
FROM prev_year_new_users u
JOIN prev_year_new_reviews r ON r.year = u.year
ORDER BY 1
"""
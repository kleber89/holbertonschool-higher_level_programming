-- 8. Cities of California
USE hbtn_0d_usa;

SELECT 
    ci.id,
    ci.name
FROM cities ci
WHERE ci.state_id = (
    SELECT st.id
    FROM states st
    WHERE st.name = 'California'
)
ORDER BY ci.id ASC;

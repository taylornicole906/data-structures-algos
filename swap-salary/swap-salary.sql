/* Write your T-SQL query statement below */

Update salary
SET sex = CASE
WHEN sex = 'm' then 'f'
when sex = 'f' then 'm'
ELSE sex end


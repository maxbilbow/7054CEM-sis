SELECT
    *
FROM
    insurance_policy AS po
LEFT JOIN insurance_package AS pa
ON
    pa.id = po.package_id
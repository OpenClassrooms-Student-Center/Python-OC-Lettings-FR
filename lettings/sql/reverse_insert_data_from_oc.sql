INSERT INTO oc_lettings_site_address (
                id,
                number,
                street,
                city,
                state,
                zip_code,
                country_iso_code
            )
            SELECT
                id,
                number,
                street,
                city,
                state,
                zip_code,
                country_iso_code
            FROM
                lettings_address;

INSERT INTO oc_lettings_site_letting (
                id,
                title,
                address_id
            )
            SELECT
                id,
                title,
                address_id
            FROM
                lettings_letting;
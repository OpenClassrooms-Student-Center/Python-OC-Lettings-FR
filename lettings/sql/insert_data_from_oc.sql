INSERT INTO lettings_address (
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
                oc_lettings_site_address;

INSERT INTO lettings_letting (
                id,
                title,
                address_id
            )
            SELECT
                id,
                title,
                address_id
            FROM
                oc_lettings_site_letting;
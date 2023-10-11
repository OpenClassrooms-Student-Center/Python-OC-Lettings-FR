INSERT INTO oc_lettings_site_profile (
                id,
                favorite_city,
                user_id
            )
            SELECT
                id,
                favorite_city,
                user_id
            FROM
                profiles_profile;

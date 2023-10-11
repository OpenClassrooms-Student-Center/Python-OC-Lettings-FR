INSERT INTO profiles_profile (
                id,
                favorite_city,
                user_id
            )
            SELECT
                id,
                favorite_city,
                user_id
            FROM
                oc_lettings_site_profile;

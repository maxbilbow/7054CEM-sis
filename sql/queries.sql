ALTER TABLE
    `user_profile` ADD CONSTRAINT `user_profile_personal_details` FOREIGN KEY(`personal_details_id`) REFERENCES `personal_details`(`id`) ON DELETE SET NULL ON UPDATE CASCADE;
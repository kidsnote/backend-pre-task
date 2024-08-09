BEGIN;
--
-- Create model Contact
--
CREATE TABLE "contact_contact" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "profile_photo" varchar(200) NULL, "name" varchar(128) NOT NULL, "company_name" varchar(128) NULL, "company_position" varchar(128) NULL, "memo" text NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Label
--
CREATE TABLE "contact_label" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(128) NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ContactWebsite
--
CREATE TABLE "contact_contactwebsite" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "website" varchar(200) NOT NULL, "contact_id" bigint NOT NULL REFERENCES "contact_contact" ("id") DEFERRABLE INITIALLY DEFERRED, "label_id" bigint NULL REFERENCES "contact_label" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ContactPhoneNumber
--
CREATE TABLE "contact_contactphonenumber" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "phone_number" varchar(128) NOT NULL, "contact_id" bigint NOT NULL REFERENCES "contact_contact" ("id") DEFERRABLE INITIALLY DEFERRED, "label_id" bigint NULL REFERENCES "contact_label" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ContactImportantDate
--
CREATE TABLE "contact_contactimportantdate" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "important_date" date NOT NULL, "contact_id" bigint NOT NULL REFERENCES "contact_contact" ("id") DEFERRABLE INITIALLY DEFERRED, "label_id" bigint NULL REFERENCES "contact_label" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ContactEmail
--
CREATE TABLE "contact_contactemail" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "email" varchar(254) NOT NULL, "contact_id" bigint NOT NULL REFERENCES "contact_contact" ("id") DEFERRABLE INITIALLY DEFERRED, "label_id" bigint NULL REFERENCES "contact_label" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ContactAddress
--
CREATE TABLE "contact_contactaddress" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "address" text NOT NULL, "contact_id" bigint NOT NULL REFERENCES "contact_contact" ("id") DEFERRABLE INITIALLY DEFERRED, "label_id" bigint NULL REFERENCES "contact_label" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create constraint name on model label
--
CREATE TABLE "new__contact_label" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(128) NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, CONSTRAINT "name" UNIQUE ("user_id", "name"));
INSERT INTO "new__contact_label" ("id", "name", "user_id") SELECT "id", "name", "user_id" FROM "contact_label";
DROP TABLE "contact_label";
ALTER TABLE "new__contact_label" RENAME TO "contact_label";
CREATE INDEX "contact_contact_user_id_2e02db50" ON "contact_contact" ("user_id");
CREATE INDEX "contact_contactwebsite_contact_id_3da02ca0" ON "contact_contactwebsite" ("contact_id");
CREATE INDEX "contact_contactwebsite_label_id_589c8e1c" ON "contact_contactwebsite" ("label_id");
CREATE INDEX "contact_contactphonenumber_contact_id_49231a12" ON "contact_contactphonenumber" ("contact_id");
CREATE INDEX "contact_contactphonenumber_label_id_50e5c8b9" ON "contact_contactphonenumber" ("label_id");
CREATE INDEX "contact_contactimportantdate_contact_id_e7b432ab" ON "contact_contactimportantdate" ("contact_id");
CREATE INDEX "contact_contactimportantdate_label_id_a1ac8d57" ON "contact_contactimportantdate" ("label_id");
CREATE INDEX "contact_contactemail_contact_id_e8c369e1" ON "contact_contactemail" ("contact_id");
CREATE INDEX "contact_contactemail_label_id_486f3544" ON "contact_contactemail" ("label_id");
CREATE INDEX "contact_contactaddress_contact_id_d6699416" ON "contact_contactaddress" ("contact_id");
CREATE INDEX "contact_contactaddress_label_id_573986f9" ON "contact_contactaddress" ("label_id");
CREATE INDEX "contact_label_user_id_f4f84742" ON "contact_label" ("user_id");
COMMIT;

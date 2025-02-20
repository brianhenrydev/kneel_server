CREATE TABLE "Metals"
(
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "metal" NVARCHAR(160) NOT NULL,
    "price" NUMERIC(5,2) NOT NULL
);

CREATE TABLE "Styles"
(
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "style" NVARCHAR(160) NOT NULL,
    "price" NUMERIC(5,2) NOT NULL
);

CREATE TABLE "Sizes"
(
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "size" NVARCHAR(160) NOT  NULL,
    "price" NUMERIC(5,2) NOT NULL
);

CREATE TABLE "Orders"
(
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "metal_id" INTEGER NOT NULL,
    "size_id" INTEGER NOT NULL,
    "style_id" INTEGER NOT NULL,
    FOREIGN KEY("metal_id") REFERENCES "Metals"("id"),
    FOREIGN KEY("size_id") REFERENCES "Sizes"("id"),
    FOREIGN KEY("style_id") REFERENCES "Styles"("id")
);

INSERT INTO "Metals" ("metal", "price") 
VALUES 
('Sterling Silver', 12.42),
('14K Gold', 736.40),
('24K Gold', 1258.90),
('Platinum', 795.45),
('Palladium', 1241.00);

INSERT INTO "Sizes" ("size", "price") 
VALUES 
('0.5', 5.00),
('0.75', 7.50),
('1', 10.00),
('1.5', 15.00),
('2', 20.00);

INSERT INTO "Styles" ("style", "price") 
VALUES 
('Classic', 500),
('Modern', 710),
('Vintage', 965);

INSERT INTO "Orders" ("metal_id", "size_id", "style_id") 
VALUES 
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 1),
(5, 5, 2);


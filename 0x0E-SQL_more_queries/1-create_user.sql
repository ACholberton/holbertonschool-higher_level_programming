-- This Script creates a user with all priviledges

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' INDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';


INSERT INTO roles (name) VALUES
('student'),
('instructor'),
('admin');

INSERT INTO permissions (name) VALUES
('VIEW_LESSONS'),
('EDIT_LESSONS'),
('VIEW_DOCUMENT'),
('DELETE_DOCUMENT');

INSERT INTO role_permissions (role_id, permission_id) VALUES
(1,1),
(1,3);

INSERT INTO role_permissions (role_id, permission_id) VALUES
(2,1),
(2,2),
(2,3);

INSERT INTO role_permissions (role_id, permission_id)
SELECT 3, id FROM permissions;

INSERT INTO users (username, password_hash) VALUES
('alice', 'hashed_pw_alice'),
('bob', 'hashed_pw_bob'),
('carol', 'hashed_pw_carol');

--alice is a student
INSERT INTO user_roles (user_id, role_id) VALUES (1,1);

--bob is an instructor
INSERT INTO user_roles (user_id, role_id) VALUES (2,2);

--carol is admin
INSERT INTO user_roles (user_id, role_id) VALUES (3,3);


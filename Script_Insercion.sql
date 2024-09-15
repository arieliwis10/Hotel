-- Insertar datos en CATEGORIA
INSERT INTO CATEGORIA (id_categoria, nombre_cat) VALUES (1, 'Turista');
INSERT INTO CATEGORIA (id_categoria, nombre_cat) VALUES (2, 'Premium');

-- Insertar el hotel con hotel_id = 1
INSERT INTO HOTEL (hotel_id, nombre, direccion, telefono) VALUES (1, 'Hotel Central', 'Av. Principal 123', 12345678);

-- Insertar datos en HABITACION
INSERT INTO HABITACION (habitacion_id, hotel_id, id_categoria, capacidad, valor, estado_habitacion) VALUES (1, 1, 1, 2, 25000, 'Disponible');
INSERT INTO HABITACION (habitacion_id, hotel_id, id_categoria, capacidad, valor, estado_habitacion) VALUES (2, 1, 2, 4, 50000, 'Disponible');
INSERT INTO HABITACION (habitacion_id, hotel_id, id_categoria, capacidad, valor, estado_habitacion) VALUES (3, 1, 1, 2, 50000, 'Ocupada');
INSERT INTO HABITACION (habitacion_id, hotel_id, id_categoria, capacidad, valor, estado_habitacion) VALUES (4, 1, 2, 4, 100000, 'Disponible');

-- Insertar datos en CLIENTE
INSERT INTO CLIENTE (cliente_id, nombre_cli, apellido_cli, correo, telefono) VALUES (1, 'Juan', 'Pérez', 'juan.perez@example.com', 987654321);
INSERT INTO CLIENTE (cliente_id, nombre_cli, apellido_cli, correo, telefono) VALUES (2, 'Ana', 'Gómez', 'ana.gomez@example.com', 987654322);

-- Insertar datos en TIPO_PAGO
INSERT INTO TIPO_PAGO (id_tipo_pago, descripcion) VALUES (1, 'Efectivo');
INSERT INTO TIPO_PAGO (id_tipo_pago, descripcion) VALUES (2, 'Credito');

-- Insertar datos en SERVICIOS
INSERT INTO SERVICIOS (id_servicio, nombre, descripcion, valor) VALUES (1, 'Spa', 'Servicio de Spa', 30000);
INSERT INTO SERVICIOS (id_servicio, nombre, descripcion, valor) VALUES (2, 'Gimnasio', 'Acceso al gimnasio', 20000);


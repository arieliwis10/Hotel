-- Insertar datos en HOTEL
INSERT INTO HOTEL (hotel_id, nombre, direccion, telefono) VALUES (1, 'Hotel Central', 'Calle Falsa 123', 123456789);

-- Insertar datos en CATEGORIA
INSERT INTO CATEGORIA (id_categoria, nombre_cat) VALUES (1, 'Económica');
INSERT INTO CATEGORIA (id_categoria, nombre_cat) VALUES (2, 'Ejecutiva');
INSERT INTO CATEGORIA (id_categoria, nombre_cat) VALUES (3, 'Lujo');

-- Insertar datos en HABITACION
INSERT INTO HABITACION (habitacion_id, hotel_id, id_categoria, capacidad, valor, estado_habitacion) VALUES (1, 1, 1, 2, 50, 'Disponible');
INSERT INTO HABITACION (habitacion_id, hotel_id, id_categoria, capacidad, valor, estado_habitacion) VALUES (2, 1, 2, 3, 100, 'Ocupada');
INSERT INTO HABITACION (habitacion_id, hotel_id, id_categoria, capacidad, valor, estado_habitacion) VALUES (3, 1, 3, 4, 200, 'Disponible');

-- Insertar datos en CLIENTE
INSERT INTO CLIENTE (cliente_id, nombre_cli, apellido_cli, correo, telefono) VALUES (1, 'Juan', 'Pérez', 'juan.perez@example.com', 987654321);
INSERT INTO CLIENTE (cliente_id, nombre_cli, apellido_cli, correo, telefono) VALUES (2, 'Ana', 'Gómez', 'ana.gomez@example.com', 987654322);

-- Insertar datos en TIPO_PAGO
INSERT INTO TIPO_PAGO (id_tipo_pago, descripcion) VALUES (1, 'Efectivo');
INSERT INTO TIPO_PAGO (id_tipo_pago, descripcion) VALUES (2, 'Tarjeta de Crédito');

-- Insertar datos en PAGO
INSERT INTO PAGO (id_pago, id_cliente, id_reserva, id_tipo_pago, fecha_pago, monto, estado_pago) VALUES (1, 1, 1, 2, TO_DATE('2024-08-30', 'YYYY-MM-DD'), 100, 'Pagado');

-- Insertar datos en SERVICIOS
INSERT INTO SERVICIOS (id_servicio, nombre, descripcion, valor) VALUES (1, 'Spa', 'Servicio de Spa', 50);
INSERT INTO SERVICIOS (id_servicio, nombre, descripcion, valor) VALUES (2, 'Gimnasio', 'Acceso al gimnasio', 20);

-- Insertar datos en RESERVA
INSERT INTO RESERVA (reserva_id, cliente_id, habitacion_id, fecha_check_in, fecha_check_out, cantidad_personas, id_pago, id_servicio, estado_reserva) VALUES 
(1, 1, 1, TO_DATE('2024-09-01', 'YYYY-MM-DD'), TO_DATE('2024-09-05', 'YYYY-MM-DD'), 2, 1, 1, 'Confirmada');

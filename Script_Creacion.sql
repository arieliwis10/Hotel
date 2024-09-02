CREATE TABLE HOTEL (
    hotel_id INTEGER PRIMARY KEY,
    nombre VARCHAR2(25),
    direccion VARCHAR2(50),
    telefono INTEGER
);

CREATE TABLE CATEGORIA (
    id_categoria INTEGER PRIMARY KEY,
    nombre_cat VARCHAR2(25)
);

CREATE TABLE HABITACION (
    habitacion_id INTEGER PRIMARY KEY,
    hotel_id INTEGER,
    id_categoria INTEGER,
    capacidad INTEGER,
    valor INTEGER,
    estado_habitacion VARCHAR2(15),
    FOREIGN KEY (hotel_id) REFERENCES HOTEL(hotel_id),
    FOREIGN KEY (id_categoria) REFERENCES CATEGORIA(id_categoria)
);

CREATE TABLE CLIENTE (
    cliente_id INTEGER PRIMARY KEY,
    nombre_cli VARCHAR2(25),
    apellido_cli VARCHAR2(25),
    correo VARCHAR2(50),
    telefono INTEGER
);

CREATE TABLE RESERVA (
    reserva_id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    habitacion_id INTEGER,
    fecha_check_in DATE,
    fecha_check_out DATE,
    cantidad_personas INTEGER,
    id_pago INTEGER,
    id_servicio INTEGER,
    estado_reserva VARCHAR2(15),
    FOREIGN KEY (cliente_id) REFERENCES CLIENTE(cliente_id),
    FOREIGN KEY (habitacion_id) REFERENCES HABITACION(habitacion_id),
    FOREIGN KEY (id_pago) REFERENCES PAGO(id_pago),
    FOREIGN KEY (id_servicio) REFERENCES SERVICIOS(id_servicio)
);

CREATE TABLE PERSONAL (
    id_personal INTEGER PRIMARY KEY,
    id_hotel INTEGER,
    nombre_per VARCHAR2(25),
    apellido_per VARCHAR2(25),
    correo VARCHAR2(50),
    telefono INTEGER,
    cargo VARCHAR2(15),
    FOREIGN KEY (id_hotel) REFERENCES HOTEL(hotel_id)
);

CREATE TABLE PAGO (
    id_pago INTEGER PRIMARY KEY,
    id_cliente INTEGER,
    id_reserva INTEGER,
    id_tipo_pago INTEGER,
    fecha_pago DATE,
    monto INTEGER,
    estado_pago VARCHAR2(15),
    FOREIGN KEY (id_cliente) REFERENCES CLIENTE(cliente_id),
    FOREIGN KEY (id_reserva) REFERENCES RESERVA(reserva_id),
    FOREIGN KEY (id_tipo_pago) REFERENCES TIPO_PAGO(id_tipo_pago)
);

CREATE TABLE TIPO_PAGO (
    id_tipo_pago INTEGER PRIMARY KEY,
    descripcion VARCHAR2(15)
);

CREATE TABLE SERVICIOS (
    id_servicio INTEGER PRIMARY KEY,
    nombre VARCHAR2(15),
    descripcion VARCHAR2(70),
    valor INTEGER
);

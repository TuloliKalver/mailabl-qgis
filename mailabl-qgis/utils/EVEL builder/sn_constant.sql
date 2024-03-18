--
-- PostgreSQL database dump
--

-- Dumped from database version 11.9 (Debian 11.9-0+deb10u1)
-- Dumped by pg_dump version 14.0

-- Started on 2021-12-02 11:21:44

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

--
-- TOC entry 613 (class 1259 OID 6822334)
-- Name: sn_constant; Type: TABLE; Schema: evel; Owner: postgres
--

CREATE TABLE evel.sn_constant (
    id integer NOT NULL,
    groupname character varying(50),
    txt character varying(60),
    parent_group character varying(50),
    descriprion character varying(50),
    orderno integer
);


ALTER TABLE evel.sn_constant OWNER TO postgres;

--
-- TOC entry 9835 (class 0 OID 0)
-- Dependencies: 613
-- Name: TABLE sn_constant; Type: COMMENT; Schema: evel; Owner: postgres
--

COMMENT ON TABLE evel.sn_constant IS 'Valikud ja eeldefineeritud andmed';


--
-- TOC entry 9836 (class 0 OID 0)
-- Dependencies: 613
-- Name: COLUMN sn_constant.id; Type: COMMENT; Schema: evel; Owner: postgres
--

COMMENT ON COLUMN evel.sn_constant.id IS 'Primaarvõti';


--
-- TOC entry 9837 (class 0 OID 0)
-- Dependencies: 613
-- Name: COLUMN sn_constant.groupname; Type: COMMENT; Schema: evel; Owner: postgres
--

COMMENT ON COLUMN evel.sn_constant.groupname IS 'Grupp';


--
-- TOC entry 9838 (class 0 OID 0)
-- Dependencies: 613
-- Name: COLUMN sn_constant.txt; Type: COMMENT; Schema: evel; Owner: postgres
--

COMMENT ON COLUMN evel.sn_constant.txt IS 'Liigid';


--
-- TOC entry 9839 (class 0 OID 0)
-- Dependencies: 613
-- Name: COLUMN sn_constant.parent_group; Type: COMMENT; Schema: evel; Owner: postgres
--

COMMENT ON COLUMN evel.sn_constant.parent_group IS 'A grupp';


--
-- TOC entry 9840 (class 0 OID 0)
-- Dependencies: 613
-- Name: COLUMN sn_constant.descriprion; Type: COMMENT; Schema: evel; Owner: postgres
--

COMMENT ON COLUMN evel.sn_constant.descriprion IS 'Selgitus';


--
-- TOC entry 9841 (class 0 OID 0)
-- Dependencies: 613
-- Name: COLUMN sn_constant.orderno; Type: COMMENT; Schema: evel; Owner: postgres
--

COMMENT ON COLUMN evel.sn_constant.orderno IS 'Järjekorra nr';


--
-- TOC entry 9829 (class 0 OID 6822334)
-- Dependencies: 613
-- Data for Name: sn_constant; Type: TABLE DATA; Schema: evel; Owner: postgres
--

INSERT INTO evel.sn_constant VALUES (0, 'BUILDING_AREA_LOCATION', 'Maa-alune', NULL, 'Rajatise paiknemine', NULL);
INSERT INTO evel.sn_constant VALUES (1, 'BUILDING_AREA_LOCATION', 'Maapealne', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (2, 'BUILDING_AREA_TYPE', 'Reovee eelpuhastid', NULL, 'Rajatise tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (3, 'BUILDING_AREA_TYPE', 'Reoveepuhastid', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (4, 'BUILDING_AREA_TYPE', 'Settetöötlus', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (5, 'BUILDING_AREA_TYPE', 'Bioloogiline puhastus', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (6, 'BUILDING_AREA_TYPE', 'Mehhaaniline puhastus', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (7, 'BUILDING_AREA_TYPE', 'Muud rajatised', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (8, 'BUILDING_AREA_TYPE_SUB', 'Rasvapüüdur', NULL, 'Rajatise alamtüüp', NULL);
INSERT INTO evel.sn_constant VALUES (9, 'BUILDING_AREA_TYPE_SUB', 'Õlipüüdur', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (10, 'BUILDING_AREA_TYPE_SUB', 'Liivapüüdur', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (11, 'BUILDING_AREA_TYPE_SUB', 'Sademevee imbväljak', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (12, 'BUILDING_AREA_TYPE_SUB', 'Sademevee mahuti', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (13, 'BUILDING_AREA_TYPE_SUB', 'Kaevurake', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (14, 'BUILDING_AREA_TYPE_SUB', 'Hülss', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (15, 'CONDITION_CLASS', '0', NULL, 'Seisukorra info', NULL);
INSERT INTO evel.sn_constant VALUES (16, 'CONDITION_CLASS', '1', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (17, 'CONDITION_CLASS', '2', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (18, 'CONDITION_CLASS', '3', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (19, 'CONDITION_CLASS', '4', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (20, 'CONSUMERPOINT_GROUP', 'Normaalarveldatavad', NULL, 'Tarbimispunkti grupp', NULL);
INSERT INTO evel.sn_constant VALUES (21, 'CONSUMERPOINT_GROUP', 'Suvevesi', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (22, 'CONSUMERPOINT_GROUP', 'Pea-ja kõrvalmõõtjaga', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (23, 'CONSUMERPOINT_STATE', 'Määramata', NULL, 'Tarbimispunkti olek', NULL);
INSERT INTO evel.sn_constant VALUES (24, 'CONSUMERPOINT_STATE', 'Aktiivne', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (25, 'CONSUMERPOINT_STATE', 'Leping sõlmimisel', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (26, 'CONSUMERPOINT_STATE', 'Kandidaat', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (27, 'CONSUMERPOINT_TYPE', 'Määramata', NULL, 'Tarbimispunkti tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (28, 'CONSUMERPOINT_TYPE', 'Ühepereelamu', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (29, 'CONSUMERPOINT_TYPE', 'Kortermaja', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (30, 'CONSUMERPOINT_TYPE', 'Tööstus', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (31, 'CONSUMERPOINT_TYPE', 'Püstikkraan', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (32, 'CONTRACT_TYPE', 'Liitumisleping', NULL, 'Lepingu tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (33, 'CONTRACT_TYPE', 'Tarbimisleping', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (34, 'CUSTOMER_ROLE', 'Määramata', NULL, 'Tarbija roll', NULL);
INSERT INTO evel.sn_constant VALUES (35, 'CUSTOMER_ROLE', 'Omanik', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (36, 'CUSTOMER_ROLE', 'Rentnik', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (37, 'CUSTOMER_STATE', 'Aktiivne', NULL, 'Tarbija olek', NULL);
INSERT INTO evel.sn_constant VALUES (38, 'CUSTOMER_STATE', 'Mitteaktiivne', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (39, 'CUSTOMER_TYPE', 'Määramata', NULL, 'Tarbija tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (40, 'CUSTOMER_TYPE', 'Era', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (41, 'CUSTOMER_TYPE', 'Äri', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (42, 'CUSTOMER_TYPE', 'Munitsipaal', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (43, 'DEVICE_TYPE', 'Määramata', NULL, 'Seadme tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (44, 'DEVICE_TYPE', 'Kompressor', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (45, 'DEVICE_TYPE', 'Segur', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (46, 'DH_DUCT_DIAMETER', '32', NULL, 'Kaugküttetoru diameeter', NULL);
INSERT INTO evel.sn_constant VALUES (47, 'DH_DUCT_DIAMETER', '50', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (48, 'DH_DUCT_DIAMETER', '65', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (49, 'DH_DUCT_DIAMETER', '80', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (50, 'DH_DUCT_DIAMETER', '90', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (51, 'DH_DUCT_DIAMETER', '100', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (52, 'DH_DUCT_DIAMETER', '110', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (53, 'DH_DUCT_DIAMETER', '125', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (54, 'DH_DUCT_DIAMETER', '150', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (55, 'DH_DUCT_DIAMETER', '200', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (56, 'DH_DUCT_DIAMETER', '250', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (57, 'DH_DUCT_DIAMETER', '800', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (58, 'DH_DUCT_DIAMETER', '1200', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (59, 'DH_DUCT_MATERIAL', 'Määramata', NULL, 'Kaugküttetoru materjal', NULL);
INSERT INTO evel.sn_constant VALUES (60, 'DH_DUCT_MATERIAL', 'Teras', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (61, 'DH_DUCT_MATERIAL', 'Plast', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (62, 'DH_DUCT_ROLE', 'Määramata', NULL, 'Kaugküttetoru roll', NULL);
INSERT INTO evel.sn_constant VALUES (63, 'DH_DUCT_ROLE', 'Pealevool', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (64, 'DH_DUCT_ROLE', 'Tagasivool', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (65, 'DH_DUCT_SHELL_DIAMETER', 'Määramata', NULL, 'Kaugküttetoru isolatsiooni läbimõõt', NULL);
INSERT INTO evel.sn_constant VALUES (66, 'DH_DUCT_SHELL_DIAMETER', '125', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (67, 'DH_DUCT_SHELL_DIAMETER', '140', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (68, 'DH_DUCT_SHELL_DIAMETER', '160', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (69, 'DH_DUCT_SHELL_DIAMETER', '180', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (70, 'DH_DUCT_SHELL_DIAMETER', '225', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (71, 'DH_DUCT_SHELL_DIAMETER', '250', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (72, 'DH_DUCT_SHELL_DIAMETER', '355', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (73, 'DH_DUCT_SHELL_TYPE', 'Isoleerimata', NULL, 'Kaugküttetoru isolatsiooni tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (74, 'DH_DUCT_SHELL_TYPE', 'Eelisoleeritud', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (75, 'DH_DUCT_SHELL_TYPE', 'Paaris eelisoleeritud', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (76, 'DH_DUCT_SHELL', 'Määramata', NULL, 'Küttetoru kesta materjal', NULL);
INSERT INTO evel.sn_constant VALUES (77, 'DH_DUCT_SHELL', 'Ruberoid', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (78, 'DH_DUCT_SHELL', 'Plast', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (79, 'DH_DUCT_SHELL_MATERIAL', 'Määramata', NULL, 'Küttetoru soojustuse materjal', NULL);
INSERT INTO evel.sn_constant VALUES (80, 'DH_DUCT_SHELL_MATERIAL', 'Vill', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (81, 'DH_DUCT_SHELL_MATERIAL', 'Vaht', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (82, 'DH_MANHOLE_DIAMETER', 'Määramata', NULL, 'Soojakaevu mõõtmed', NULL);
INSERT INTO evel.sn_constant VALUES (83, 'DH_MANHOLE_DIAMETER', '3000x3000 ', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (84, 'DH_MANHOLE_DIAMETER', '700', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (85, 'DH_MANHOLE_TYPE', 'Määramata', NULL, 'Soojakaevu tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (86, 'DH_MANHOLE_TYPE', 'Kamber', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (87, 'DH_METER_TYPE', 'Määramata', NULL, 'Soojaarvesti tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (88, 'DH_METER_TYPE', 'Mehaaniline', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (89, 'DH_METER_TYPE', 'Ultraheli', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (90, 'DH_NODE_GROUP', 'Liitmikud', NULL, 'Küttesõlme grupp', NULL);
INSERT INTO evel.sn_constant VALUES (91, 'DH_NODE_GROUP', 'Sulgeseadmed', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (92, 'DH_NODE_GROUP', 'Seadmed', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (93, 'DH_NODE_GROUP', 'Rajatised', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (94, 'DH_NODE_GROUP', 'Muu', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (95, 'DH_NODE_TYPE', 'Hargmik', 'Liitmikud', 'Küttesõlme alamgrupp', NULL);
INSERT INTO evel.sn_constant VALUES (96, 'DH_NODE_TYPE', 'Pimeots', 'Liitmikud', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (97, 'DH_NODE_TYPE', 'Läbimõõdu üleminek', 'Liitmikud', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (98, 'DH_NODE_TYPE', 'Maakraan', 'Sulgeseade', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (99, 'DH_NODE_TYPE', 'Peasiiber', 'Sulgeseade', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (100, 'DH_NODE_TYPE', 'Majaühenduse siiber', 'Sulgeseade', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (101, 'DH_NODE_TYPE', 'Teenindussõlm', 'Rajatis', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (102, 'DH_NODE_TYPE', 'Kaugküttekilp', 'Rajatis', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (103, 'DH_NODE_TYPE', 'Mõõtekarp', 'Muu', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (104, 'DIAMETER_TYPE', 'De', NULL, 'Läbimõõdu tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (105, 'DIAMETER_TYPE', 'Di', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (106, 'DIAMETER_TYPE', 'Dn', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (107, 'DUCT_TYPE', 'Tüvitoru', NULL, 'Otstarve', NULL);
INSERT INTO evel.sn_constant VALUES (108, 'DUCT_TYPE', 'Peatoru', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (109, 'DUCT_TYPE', 'Ühendustoru', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (110, 'DUCT_TYPE', 'Tarbijatoru', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (111, 'DUCT_TYPE', 'Kraav', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (112, 'DUCT_TYPE', 'Renn', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (113, 'EL_CABLE_MARK', 'Määramata', NULL, 'Elektrikaabli mark', NULL);
INSERT INTO evel.sn_constant VALUES (114, 'EL_CABLE_MARK', 'AXPK-4G25', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (115, 'EL_CABLE_MARK', 'AXPK-4G35', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (116, 'EL_MAIN_FUSE_TYPE', 'Määramata', NULL, 'Peakaitsme suurus', NULL);
INSERT INTO evel.sn_constant VALUES (117, 'EL_MAIN_FUSE_TYPE', '10', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (118, 'EL_MAIN_FUSE_TYPE', '20', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (119, 'EL_METER_TYPE', 'Määramata', NULL, 'Elektriarvesti tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (120, 'EL_METER_TYPE', 'Mehaaniline', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (121, 'EL_METER_TYPE', 'Digitaalne', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (122, 'EL_NODE_GROUP', 'Alajaam', NULL, 'Elektrisõlme grupp', NULL);
INSERT INTO evel.sn_constant VALUES (123, 'EL_NODE_GROUP', 'Kilp', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (124, 'EL_NODE_GROUP', 'Muhv', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (125, 'EL_NODE_GROUP', 'Valguskoht', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (126, 'EL_NODE_TYPE', 'Mastalajaam', 'Alajaam', 'Elektrisõlme alamgrupp', NULL);
INSERT INTO evel.sn_constant VALUES (127, 'EL_NODE_TYPE', 'Alajaam', 'Alajaam', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (128, 'EL_NODE_TYPE', 'Jaotuskilp', 'Kilp', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (129, 'EL_NODE_TYPE', 'Liitumiskilp', 'Kilp', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (130, 'EL_NODE_TYPE', 'Post', 'Valguskoht', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (131, 'EL_NODE_TYPE', 'Sein', 'Valguskoht', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (132, 'EL_NODE_TYPE', 'Riputus', 'Valguskoht', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (133, 'EL_NODE_TYPE', 'Maa', 'Valguskoht', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (134, 'EXT_DOC_CATEGORY', 'Üldine', NULL, 'Dokumentide kategooria', NULL);
INSERT INTO evel.sn_constant VALUES (135, 'EXT_DOC_CATEGORY', 'Leping', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (136, 'EXT_DOC_TYPE', 'Teostusjoonis', NULL, 'Dokumentide tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (137, 'EXT_DOC_TYPE', 'Foto', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (138, 'EXT_DOC_TYPE', 'DigiDoc', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (139, 'FAILURE_CAUSE', 'Määramata', NULL, 'Rikke põhjus', NULL);
INSERT INTO evel.sn_constant VALUES (140, 'FAILURE_CAUSE', 'Külmumine', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (141, 'FAILURE_CAUSE', 'Lõhkumine', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (142, 'FAILURE_CAUSE', 'Ummistus', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (143, 'FAILURE_NOT_VALID', 'Kuulub lahendamisele', NULL, 'Vea kuuluvus', NULL);
INSERT INTO evel.sn_constant VALUES (144, 'FAILURE_NOT_VALID', 'Ei kuulu lahendamisele', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (145, 'FAILURE_SEVERITY', 'Määramata', NULL, 'Raskusaste', NULL);
INSERT INTO evel.sn_constant VALUES (146, 'FAILURE_SEVERITY', 'Kerge', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (147, 'FAILURE_SEVERITY', 'Keskmine', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (148, 'FAILURE_SEVERITY', 'Vajab kohest sekkumist', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (149, 'FAILURE_SEVERITY', 'Raske', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (150, 'FAILURE_TYPE', 'Määramata', NULL, 'Vea tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (151, 'FAILURE_TYPE', 'Leke', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (152, 'FAILURE_TYPE', 'Madal surve', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (153, 'FAILURE_TYPE', 'Ummistus', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (154, 'FIRE_PLUG_LOCATION', 'Määramata', NULL, 'Hüdrandi paiknemine', NULL);
INSERT INTO evel.sn_constant VALUES (155, 'FIRE_PLUG_LOCATION', 'Maapealne', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (156, 'FIRE_PLUG_LOCATION', 'Hoonel', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (157, 'FIRE_PLUG_LOCATION', 'Kaevus', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (158, 'FIRE_PLUG_TYPE', 'Määramata', NULL, 'Hüdrandi tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (159, 'FIRE_PLUG_TYPE', 'Tuletõrjehüdrant', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (160, 'FIRE_PLUG_TYPE_SUB', 'Määramata', NULL, 'Hüdrandi alamtüüp', NULL);
INSERT INTO evel.sn_constant VALUES (161, 'FIRE_PLUG_TYPE_SUB', 'T', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (162, 'FIRE_PLUG_TYPE_SUB', 'TS', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (163, 'FIRMNESS_CLASS', 'Määramata', NULL, 'Ringjäikus', NULL);
INSERT INTO evel.sn_constant VALUES (164, 'FLOWMETER_CLASS', 'Määramata', NULL, 'Veemõõtja klass', NULL);
INSERT INTO evel.sn_constant VALUES (165, 'FLOWMETER_CLASS', 'Peaarvesti', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (166, 'FLOWMETER_CLASS', 'Kõrvalarvesti', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (167, 'FLOWMETER_CONSOLE', 'Määramata', NULL, 'Veearvesti konsooli pikkus', NULL);
INSERT INTO evel.sn_constant VALUES (168, 'FLOWMETER_CONSOLE', '175', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (169, 'FLOWMETER_SIZE', 'Määramata', NULL, 'Veearvesti toru läbimõõt', NULL);
INSERT INTO evel.sn_constant VALUES (170, 'FLOWMETER_SIZE', 'DN10', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (171, 'FLOWMETER_SIZE', 'DN15', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (172, 'FLOWMETER_SIZE', 'DN20', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (173, 'FLOWMETER_SIZE', 'DN25', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (174, 'FLOWMETER_SIZE', 'DN32', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (175, 'FLOWMETER_SIZE', 'DN40', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (176, 'FLOWMETER_SIZE', 'DN50', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (177, 'FLOWMETER_SIZE', 'DN63', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (178, 'FLOWMETER_SIZE', 'DN100', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (179, 'FLOWMETER_SIZE', 'DN160', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (180, 'FLOWMETER_SIZE', 'DN200', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (181, 'FLOWMETER_TYPE', 'Määramata', NULL, 'Veemõõtja tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (182, 'FLOWMETER_TYPE', 'Mehaaniline', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (183, 'FLOWMETER_TYPE', 'Ultraheli', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (184, 'FLOWMETER_WATER_TYPE', 'Määramata', NULL, 'Mõõdetava vee liik', NULL);
INSERT INTO evel.sn_constant VALUES (185, 'FLOWMETER_WATER_TYPE', 'Joogivesi', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (186, 'FLOWMETER_WATER_TYPE', 'Kastmisvesi', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (187, 'FLOWMETER_WATER_TYPE', 'Toorvesi', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (188, 'FLOWMETER_WATER_TYPE', 'Reovesi', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (189, 'FORM_CODE', 'Määramata', NULL, 'Toru kuju', NULL);
INSERT INTO evel.sn_constant VALUES (190, 'FORM_CODE', 'Ümmargune', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (191, 'FORM_CODE', 'Neljakandiline', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (192, 'FREE_AREA_TYPE', 'Tegevuspiirkond', NULL, 'Piirkondade tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (193, 'FREE_AREA_TYPE', 'Veehaardeala', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (194, 'FREE_AREA_TYPE', 'Reoveekogumisala', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (195, 'FREE_AREA_TYPE', 'Sanitaarkaitseala', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (196, 'FREE_AREA_TYPE', 'Kuja', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (197, 'FREE_AREA_TYPE', 'Niitmisala', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (198, 'FREE_AREA_TYPE', 'Lumekoristusala', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (199, 'FREE_LINE_TYPE', 'Märkejoon', NULL, 'Vaba joone tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (200, 'FREE_LINE_TYPE', 'Maanduskontuur', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (201, 'GAS_DUCT_DIAMETER', '20', NULL, 'Gaasitoru diameeter', NULL);
INSERT INTO evel.sn_constant VALUES (202, 'GAS_DUCT_DIAMETER', '25', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (203, 'GAS_DUCT_DIAMETER', '32', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (204, 'GAS_DUCT_DIAMETER', '40', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (205, 'GAS_DUCT_DIAMETER', '50', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (206, 'GAS_DUCT_DIAMETER', '63', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (207, 'GAS_DUCT_DIAMETER', '75', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (208, 'GAS_DUCT_DIAMETER', '90', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (209, 'GAS_DUCT_DIAMETER', '100', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (210, 'GAS_DUCT_DIAMETER', '110', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (211, 'GAS_DUCT_DIAMETER', '125', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (212, 'GAS_DUCT_DIAMETER', '140', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (213, 'GAS_DUCT_DIAMETER', '160', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (214, 'GAS_DUCT_DIAMETER', '180', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (215, 'GAS_DUCT_DIAMETER', '200', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (216, 'GAS_DUCT_DIAMETER', '225', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (217, 'GAS_DUCT_MATERIAL', 'Määramata', NULL, 'Gaasitoru materjal', NULL);
INSERT INTO evel.sn_constant VALUES (218, 'GAS_DUCT_MATERIAL', 'Teras', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (219, 'GAS_DUCT_MATERIAL', 'Plast', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (220, 'GAS_MANHOLE_DIAMETER', 'Määramata', NULL, 'Gaasikaevu mõõtmed', NULL);
INSERT INTO evel.sn_constant VALUES (221, 'GAS_MANHOLE_DIAMETER', '3000x3000 ', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (222, 'GAS_MANHOLE_DIAMETER', '1000', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (223, 'GAS_MANHOLE_DIAMETER', '1500', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (224, 'GAS_MANHOLE_DIAMETER', '2000', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (225, 'GAS_MANHOLE_TYPE', 'Gaasikaev', NULL, 'Gaasikaevu tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (226, 'GAS_METER_TYPE', 'Määramata', NULL, 'Gaasiarvesti tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (227, 'GAS_METER_TYPE', 'Membraan', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (228, 'GAS_METER_TYPE', 'Rootor', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (229, 'GAS_METER_TYPE', 'Turbiin', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (230, 'GAS_METER_TYPE', 'Ultraheli', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (231, 'GAS_NODE_GROUP', 'Liitmikud', NULL, 'Gaasisõlme grupp', NULL);
INSERT INTO evel.sn_constant VALUES (232, 'GAS_NODE_GROUP', 'Sulgeseadmed', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (233, 'GAS_NODE_GROUP', 'Seadmed', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (234, 'GAS_NODE_GROUP', 'Rajatised', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (235, 'GAS_NODE_TYPE', 'Muhv', 'Liitmikud', 'Gaasisõlme alamgrupp', NULL);
INSERT INTO evel.sn_constant VALUES (236, 'GAS_NODE_TYPE', 'Pimeots', 'Liitmikud', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (237, 'GAS_NODE_TYPE', 'Läbimõõdu üleminek', 'Liitmikud', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (238, 'GAS_NODE_TYPE', 'Maakraan', 'Sulgeseade', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (239, 'GAS_NODE_TYPE', 'Peasiiber', 'Sulgeseade', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (240, 'GAS_NODE_TYPE', 'Majaühenduse siiber', 'Sulgeseade', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (241, 'GAS_NODE_TYPE', 'Gaasijaotusjaam', 'Rajatis', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (242, 'GAS_NODE_TYPE', 'Gaasikapp', 'Rajatis', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (243, 'GAS_NODE_TYPE', 'Hüdrolukk', 'Seade', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (244, 'GAS_NODE_TYPE', 'W-kondensaadikogur', 'Seade', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (245, 'GAS_NODE_TYPE', 'Andmeedastusseade', 'Seade', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (246, 'GAS_NODE_TYPE', 'Katoodkaitsemuundur', 'Seade', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (247, 'GAS_PRESSURE_CLASS', 'Määramata', NULL, 'Gaasi surveklass', NULL);
INSERT INTO evel.sn_constant VALUES (248, 'GAS_PRESSURE_CLASS', 'A', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (249, 'GAS_PRESSURE_CLASS', 'B', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (250, 'GAS_PRESSURE_CLASS', 'C', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (251, 'GAS_PRESSURE_CLASS', 'D', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (252, 'HEIGHT_ACCURACY', 'Määramata', NULL, 'Kõrguse täpsus', NULL);
INSERT INTO evel.sn_constant VALUES (253, 'HEIGHT_ACCURACY', '2 cm', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (254, 'HEIGHT_ACCURACY', '5 cm', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (255, 'HEIGHT_ACCURACY', '10 cm', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (256, 'HEIGHT_ACCURACY', '50 cm', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (257, 'HEIGHT_ACCURACY', '1 m', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (258, 'HEIGHT_ACCURACY', '5 m', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (259, 'LAND_PERM_STATE', 'Tegemisel', NULL, 'Servituudi olek', NULL);
INSERT INTO evel.sn_constant VALUES (260, 'LAND_PERM_STATE', 'Sõlmitud', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (261, 'LAND_PERM_TYPE', 'Lihtkirjalik', NULL, 'Servituudi liik', NULL);
INSERT INTO evel.sn_constant VALUES (262, 'LAND_PERM_TYPE', 'Notariaalne', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (263, 'LAND_PERM_TYPE', 'Seadusest tulenev', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (264, 'LAND_PERM_TYPE', 'Sundvaldus', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (265, 'LID_CAPACITY', 'Määramata', NULL, 'Kaane kandevõime', NULL);
INSERT INTO evel.sn_constant VALUES (266, 'LID_CAPACITY', '25', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (267, 'LID_CAPACITY', '40', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (268, 'LID_DIAMETER', '200', NULL, 'Kaane mõõtmed', NULL);
INSERT INTO evel.sn_constant VALUES (269, 'LID_DIAMETER', '400', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (270, 'LID_DIAMETER', '500', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (271, 'LID_DIAMETER', '600', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (272, 'LID_DIAMETER', '640', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (273, 'LID_DIAMETER', '700', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (274, 'LID_DIAMETER', '800', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (275, 'LID_MATERIAL', 'Määramata', NULL, 'Kaane materjal', NULL);
INSERT INTO evel.sn_constant VALUES (276, 'LID_MATERIAL', 'Betoon', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (277, 'LID_MATERIAL', 'Malm', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (278, 'LID_MATERIAL', 'Plast', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (279, 'LID_MATERIAL', 'Puit', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (280, 'LID_MATERIAL', 'Teras', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (281, 'LID_SHAPE', 'Määramata', NULL, 'Kaane kuju', NULL);
INSERT INTO evel.sn_constant VALUES (282, 'LID_SHAPE', 'Ümar', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (283, 'LID_SHAPE', 'Nelinurkne', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (284, 'LID_TYPE', 'Määramata', NULL, 'Kaane tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (285, 'LID_TYPE', 'Rest', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (286, 'LID_TYPE', 'Kinnine', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (287, 'LIGHT_MARK', 'Teadmata', NULL, 'Valgusti mark', NULL);
INSERT INTO evel.sn_constant VALUES (288, 'LIGHT_TYPE', 'Määramata', NULL, 'Valgusti tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (289, 'LIGHT_TYPE', 'Led', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (290, 'LIGHT_TYPE', 'Halogeen', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (291, 'LIGHT_TYPE', 'Naatrium', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (292, 'LOCATION', 'Maapealne', NULL, 'Toru või kaabli paiknemine', NULL);
INSERT INTO evel.sn_constant VALUES (293, 'LOCATION', 'Maa-alune', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (294, 'LOCATION', 'Veealune', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (295, 'LOCATION', 'Hoones', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (296, 'LOCATION', 'Õhus', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (297, 'LOCATION', 'Torus', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (298, 'LOCATION', 'Künas', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (299, 'LOCATION_ACCURACY', 'Määramata', NULL, 'Asukoha täpsus', NULL);
INSERT INTO evel.sn_constant VALUES (300, 'LOCATION_ACCURACY', '2 cm', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (301, 'LOCATION_ACCURACY', '10 cm', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (302, 'LOCATION_ACCURACY', '50 cm', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (303, 'LOCATION_ACCURACY', '1 m', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (304, 'LOCATION_ACCURACY', '5 m', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (305, 'MAPPING_METHOD', 'Määramata', NULL, 'Kaardistuse meetod', NULL);
INSERT INTO evel.sn_constant VALUES (306, 'MAPPING_METHOD', 'Teostusjoonis', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (307, 'MAPPING_METHOD', 'Digitud', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (308, 'NET_TYPE', 'Surve', NULL, 'Võrgu tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (309, 'NET_TYPE', 'Isevoolne', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (310, 'NET_TYPE', 'Vaakum', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (311, NULL, NULL, NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (312, 'NETWORK', 'Vesi', NULL, 'Võrk', NULL);
INSERT INTO evel.sn_constant VALUES (313, 'NETWORK', 'Tuletõrjevesi', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (314, 'NETWORK', 'Toorvesi', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (315, 'NETWORK', 'Reovesi', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (316, 'NETWORK', 'Sademevesi', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (317, 'NETWORK', 'Drenaaž', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (318, 'NETWORK', 'Ühisvoolne', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (319, 'NETWORK', 'Tänavavalgustus', NULL, 'Teenindatav võrk', NULL);
INSERT INTO evel.sn_constant VALUES (320, 'NETWORK', 'Elekter', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (321, 'OPEN_STATE', 'Määramata', NULL, 'Sõlme olek', NULL);
INSERT INTO evel.sn_constant VALUES (322, 'OPEN_STATE', 'Avatud', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (323, 'OPEN_STATE', 'Suletud', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (324, 'OPERATION', 'Määramata', NULL, 'Avarii/remonttöö liik', NULL);
INSERT INTO evel.sn_constant VALUES (325, 'OPERATION', 'Läbipesu', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (326, 'OPERATION', 'Remondimuhvi paigaldus', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (327, 'OPERATION', 'Läbikeeramine', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (328, 'OPERATION', 'Puhastamine', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (329, 'OWNER', 'Määramata', NULL, 'Omanik', NULL);
INSERT INTO evel.sn_constant VALUES (330, 'OWNER', 'Veevärk', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (331, 'OWNER', 'Klient', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (332, 'OWNER', 'Arendaja', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (333, 'OWNER', 'Teine veevärk', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (334, 'OWNER', 'KOV', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (335, 'LESSEE', 'Määramata', NULL, 'Rentnik', NULL);
INSERT INTO evel.sn_constant VALUES (336, 'LESSEE', 'Veevärk', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (337, 'LESSEE', 'Teine veevärk', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (338, 'PLAN_STATE', 'Projekteerimisel', NULL, 'Graafiliste andmete olek', NULL);
INSERT INTO evel.sn_constant VALUES (339, 'PLAN_STATE', 'Töös', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (340, 'PLAN_STATE', 'Valmis', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (341, 'PLAN_STATE', 'Kasutusest eemaldatud', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (342, 'PLAN_TYPE', 'Määramata', NULL, 'Graafiliste andmete tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (343, 'PLAN_TYPE', 'Projekt', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (344, 'PLAN_TYPE', 'Geoalus', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (345, 'PLAN_TYPE', 'Teostusjoonis', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (346, 'PLAN_TYPE', 'Muu', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (347, 'POLE_MATERIAL', 'Määramata', NULL, 'Posti materjal', NULL);
INSERT INTO evel.sn_constant VALUES (348, 'POLE_MATERIAL', 'Puit', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (349, 'POLE_MATERIAL', 'Betoon', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (350, 'POLE_MATERIAL', 'Metall', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (351, 'POLE_MATERIAL', 'Plastik', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (352, 'POLE_STANCHION_TYPE', 'Määramata', NULL, 'Jalandi tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (353, 'POLE_STANCHION_TYPE', 'Betoon', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (354, 'POLE_STANCHION_TYPE', 'Puit', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (355, 'POLE_STANCHION_TYPE', 'Teras', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (356, 'POLE_STANCHION_TYPE', 'RBJ-4', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (357, 'PRESSURE_CLASS', 'PN6', NULL, 'Rõhuklass', NULL);
INSERT INTO evel.sn_constant VALUES (358, 'PRESSURE_CLASS', 'PN10', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (359, 'PRESSURE_CLASS', 'PN16', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (360, 'PROGRAM_GROUP', 'Määramata', NULL, 'Hooldustööde grupp', NULL);
INSERT INTO evel.sn_constant VALUES (361, 'PROGRAM_GROUP', 'Hooldustööd', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (362, 'PROGRAM_GROUP', 'Renoveerimistööd', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (363, 'PS_MATERIAL', 'Määramata', NULL, 'Pumbajaama materjal', NULL);
INSERT INTO evel.sn_constant VALUES (364, 'PS_MATERIAL', 'Betoon', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (365, 'PS_MATERIAL', 'Puit', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (366, 'PS_MATERIAL', 'Tellis', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (367, 'PS_MATERIAL', 'Plastik', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (368, 'PS_MATERIAL', 'Klaaskiud', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (369, 'PS_ROLE', 'Määramata', NULL, 'Pumbajaama roll', NULL);
INSERT INTO evel.sn_constant VALUES (370, 'PS_ROLE', 'Peapumpla', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (371, 'PS_ROLE', 'Vahepumpla', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (372, 'PS_ROLE', 'Rõhutõstepumpla', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (373, 'PS_WATER_SOURCE', 'Määramata', NULL, 'Veeallikas', NULL);
INSERT INTO evel.sn_constant VALUES (374, 'PS_WATER_SOURCE', 'Veekogu', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (375, 'PS_WATER_SOURCE', 'Põhjavesi', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (376, 'PS_WATER_TYPE', 'Määramata', NULL, 'Vee tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (377, 'PS_WATER_TYPE', 'Toorvesi', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (378, 'PS_WATER_TYPE', 'Olmevesi', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (379, 'PS_WATER_TYPE', 'Tehnovesi', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (380, 'PS_WATER_TYPE', 'Tuletõrjevesi', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (381, 'PUMP_INSTALL_METHOD', 'Määramata', NULL, 'Pumba paigaldusviis', NULL);
INSERT INTO evel.sn_constant VALUES (382, 'PUMP_INSTALL_METHOD', 'Kuiv', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (383, 'PUMP_INSTALL_METHOD', 'Märg', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (384, 'STATE_INFO', 'Avarii', NULL, 'Sõlme oleku info', NULL);
INSERT INTO evel.sn_constant VALUES (385, 'STATE_INFO', 'Maksmata arve', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (386, 'SURVEY_STANDARD', 'Määramata', NULL, 'Mõõdistuse standard', NULL);
INSERT INTO evel.sn_constant VALUES (387, 'SURVEY_STANDARD', 'MKM/BK77', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (388, 'SURVEY_STANDARD', 'MKM/EH2000', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (389, 'SURVEY_STANDARD', 'MKM/EH2000/EVEL', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (390, 'SURVEY_TYPE', 'Geoalus', NULL, 'Joonise tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (391, 'SURVEY_TYPE', 'Teostusjoonis', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (392, 'SW_BRANCH_TYPE', 'Määramata', NULL, 'Kanalisatsiooni liitmiku tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (393, 'SW_BRANCH_TYPE', 'Remondimuhv', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (394, 'SW_BRANCH_TYPE', 'Pimeots/Pimeäärik', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (395, 'SW_BRANCH_TYPE', 'Ühenduskoht', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (396, 'SW_BRANCH_TYPE_SUB', 'Määramata', NULL, 'Kanalisatsiooni liitmiku alamtüüp', NULL);
INSERT INTO evel.sn_constant VALUES (397, 'SW_DUCT_DIAMETER', '100', NULL, 'Kanali toru diameeter', NULL);
INSERT INTO evel.sn_constant VALUES (398, 'SW_DUCT_DIAMETER', '110', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (399, 'SW_DUCT_DIAMETER', '125', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (400, 'SW_DUCT_DIAMETER', '150', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (401, 'SW_DUCT_DIAMETER', '160', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (402, 'SW_DUCT_DIAMETER', '200', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (403, 'SW_DUCT_DIAMETER', '225', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (404, 'SW_DUCT_DIAMETER', '250', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (405, 'SW_DUCT_DIAMETER', '280', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (406, 'SW_DUCT_DIAMETER', '300', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (407, 'SW_DUCT_DIAMETER', '315', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (408, 'SW_DUCT_DIAMETER', '350', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (409, 'SW_DUCT_DIAMETER', '400', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (410, 'SW_DUCT_DIAMETER', '450', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (411, 'SW_DUCT_DIAMETER', '500', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (412, 'SW_DUCT_DIAMETER', '570', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (413, 'SW_DUCT_DIAMETER', '600', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (414, 'SW_DUCT_DIAMETER', '700', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (415, 'SW_DUCT_DIAMETER', '800', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (416, 'SW_DUCT_DIAMETER', '900', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (417, 'SW_DUCT_DIAMETER', '1000', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (418, 'SW_DUCT_DIAMETER', '1200', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (419, 'SW_DUCT_DIAMETER', '1500', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (420, 'SW_DUCT_DIAMETER', '1800', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (421, 'SW_DUCT_DIAMETER', '2000', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (422, 'SW_DUCT_DIAMETER', '2300', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (423, 'SW_DUCT_MATERIAL', 'Määramata', NULL, 'Kanalitoru materjal', NULL);
INSERT INTO evel.sn_constant VALUES (424, 'SW_DUCT_MATERIAL', 'Betoon', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (425, 'SW_DUCT_MATERIAL', 'Teras', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (426, 'SW_DUCT_MATERIAL', 'Malm', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (427, 'SW_DUCT_MATERIAL', 'Moodul', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (428, 'SW_DUCT_MATERIAL', 'Komposiit', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (429, 'SW_DUCT_MATERIAL', 'KER', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (430, 'SW_DUCT_MATERIAL', 'Sukk', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (431, 'SW_DUCT_MATERIAL', 'ASB', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (432, 'SW_DUCT_MATERIAL', 'PE', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (433, 'SW_DUCT_MATERIAL', 'PP', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (434, 'SW_DUCT_MATERIAL', 'PVC', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (435, 'SW_DUCT_MATERIAL', 'PE RC', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (436, 'SW_MANHOLE_DIAMETER', '200', NULL, 'Kanalikaevu diameeter', NULL);
INSERT INTO evel.sn_constant VALUES (437, 'SW_MANHOLE_DIAMETER', '400', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (438, 'SW_MANHOLE_DIAMETER', '500', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (439, 'SW_MANHOLE_DIAMETER', '600', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (440, 'SW_MANHOLE_DIAMETER', '800', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (441, 'SW_MANHOLE_DIAMETER', '1000', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (442, 'SW_MANHOLE_DIAMETER', '1500', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (443, 'SW_MANHOLE_DIAMETER', '2000', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (444, 'SW_MANHOLE_DIAMETER', '2500', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (445, 'SW_MANHOLE_DIAMETER', '3000', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (446, 'MANHOLE_MATERIAL', 'Määramata', NULL, 'Kaevu materjal', NULL);
INSERT INTO evel.sn_constant VALUES (447, 'MANHOLE_MATERIAL', 'Betoon rõngas', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (448, 'MANHOLE_MATERIAL', 'Betoon monoliit', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (449, 'MANHOLE_MATERIAL', 'Pritsbetoon', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (450, 'MANHOLE_MATERIAL', 'Tellis', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (451, 'MANHOLE_MATERIAL', 'Komposiit', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (452, 'MANHOLE_MATERIAL', 'Plast', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (453, 'MANHOLE_MATERIAL', 'PVC', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (454, 'MANHOLE_MATERIAL', 'PE', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (455, 'MANHOLE_MATERIAL', 'Puit', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (456, 'SW_MANHOLE_TYPE', 'Määramata', NULL, 'Kanali kaevu tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (457, 'SW_MANHOLE_TYPE', 'Restkaev', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (458, 'SW_MANHOLE_TYPE', 'Survekustutuskaev', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (459, 'SW_MANHOLE_TYPE', 'Hoolduskaev', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (460, 'SW_MANHOLE_TYPE', 'Astangkaev', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (461, 'SW_MANHOLE_TYPE', 'Kontrollkaev', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (462, 'SW_MANHOLE_TYPE', 'Kontrolltoru', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (463, 'SW_MANHOLE_TYPE', 'Vaakumkaev', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (464, 'SW_OTHER_NODE_TYPE', 'Määramata', NULL, 'Kanali muude punktobjektide tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (465, 'SW_OTHER_NODE_TYPE', 'Kaitsearmatuur', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (466, 'SW_OTHER_NODE_TYPE', 'Suubla', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (467, 'SW_OTHER_NODE_TYPE_SUB', 'Määramata', NULL, 'Kanali muude punktobjektide alamtüüp', NULL);
INSERT INTO evel.sn_constant VALUES (468, 'SW_OTHER_NODE_TYPE_SUB', 'Õhueraldusklapp', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (469, 'SW_OTHER_NODE_TYPE_SUB', 'Tagasilöögiklapp', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (470, 'SW_PS_CONTROL', 'Määramata', NULL, 'Pumbajaama juhitavus', NULL);
INSERT INTO evel.sn_constant VALUES (471, 'SW_PS_CONTROL', 'Kaugjuhitav', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (472, 'SW_PS_CONTROL', 'Automaatne', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (473, 'SW_PS_CONTROL', 'Käsijuhtimine', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (474, 'SW_PS_ROLE', 'Määramata', NULL, 'Pumbajaama roll', NULL);
INSERT INTO evel.sn_constant VALUES (475, 'SW_PS_ROLE', 'Liini pumbajaam', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (476, 'SW_PS_ROLE', 'Vahepumbajaam', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (477, 'SW_PS_ROLE', 'Peapumpla', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (478, 'SW_PS_TYPE', 'Määramata', NULL, 'Kanalisatsioonipumpla tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (479, 'SW_PS_TYPE', 'Kanalisatsiooni pumpla', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (480, 'SW_PS_TYPE', 'Sademevee pumpla', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (481, 'SW_PS_TYPE', 'Vaakumpumpla', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (482, 'SW_PUMP_TYPE', 'Määramata', NULL, 'Tööratta tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (483, 'SW_PUMP_TYPE', 'Ühe kanaliga', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (484, 'SW_PUMP_TYPE', 'Kahe kanaliga', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (485, 'SW_PUMP_TYPE', 'Kolme kanaliga', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (486, 'SW_PUMP_TYPE', 'Keevis', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (487, 'SW_PUMP_TYPE', 'Vortex', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (488, 'SW_VALVE_TYPE', 'Määramata', NULL, 'Kanali sulgeseadme liik', NULL);
INSERT INTO evel.sn_constant VALUES (489, 'SW_VALVE_TYPE', 'Õhutuskraan', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (490, 'SW_VALVE_TYPE', 'Siiber', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (491, 'SW_VALVE_TYPE', 'Kilpsiiber', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (492, 'SW_VALVE_TYPE', 'Tagasivooluklapp', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (493, 'SW_VALVE_TYPE_SUB', 'Määramata', NULL, 'Kanali sulgeseadme alamliik', NULL);
INSERT INTO evel.sn_constant VALUES (494, 'SW_VALVE_TYPE_SUB', 'Kiil', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (495, 'SW_VALVE_TYPE_SUB', 'Klapp', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (496, 'TEL_CABLE_MARK', 'Määramata', NULL, 'Sidekaabli mark', NULL);
INSERT INTO evel.sn_constant VALUES (497, 'TEL_CABLE_MARK', 'GNHLDV 24 G652.D', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (498, 'TEL_CABLE_MARK', 'OPTRAL 48 ABD', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (499, 'TEL_CABLE_TYPE', 'Määramata', NULL, 'Sidekaabli tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (500, 'TEL_CABLE_TYPE', 'Optika', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (501, 'TEL_CABLE_TYPE', 'Vask', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (502, 'TEL_LOCATION', 'Kaev', NULL, 'Paigalduskoht', NULL);
INSERT INTO evel.sn_constant VALUES (503, 'TEL_LOCATION', 'Välikapp', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (504, 'TEL_LOCATION', 'Sisekapp', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (505, 'TEL_LOCATION', 'Post', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (506, 'TEL_NODE_GROUP', 'Jaotuskoht', NULL, 'Sidesõlme grupp', NULL);
INSERT INTO evel.sn_constant VALUES (507, 'TEL_NODE_GROUP', 'Võrgusõlm', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (508, 'TEL_NODE_GROUP', 'Muhv', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (509, 'TEL_NODE_GROUP', 'Sidekaev', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (510, 'TEL_NODE_TYPE', 'VK600', 'Jaotuskoht', 'Sidesõlme alamgrupp', NULL);
INSERT INTO evel.sn_constant VALUES (511, 'TEL_NODE_TYPE', 'VK400', 'Jaotuskoht', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (512, 'TEL_NODE_TYPE', 'VK1500', 'Jaotuskoht', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (513, 'TEL_NODE_TYPE', 'Otsejätk', 'Muhv', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (514, 'TEL_NODE_TYPE', 'Harujätk', 'Muhv', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (515, 'TEL_NODE_TYPE', 'Splitter', 'Muhv', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (516, 'TEL_NODE_TYPE', 'Sidekaev', 'Sidekaev', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (517, 'TEL_NODE_TYPE', 'Reservkaev', 'Sidekaev', NULL, NULL);
INSERT INTO evel.sn_constant VALUES (518, 'USAGE_STATE', 'Kasutusel', NULL, 'Kasutuse olek', NULL);
INSERT INTO evel.sn_constant VALUES (519, 'USAGE_STATE', 'Planeeritud', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (520, 'USAGE_STATE', 'Kasutusest kõrvaldatud', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (521, 'USAGE_STATE', 'Likvideeritud', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (522, 'W_BRANCH_TYPE', 'Määramata', NULL, 'Liitmiku tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (523, 'W_BRANCH_TYPE', 'Käänik', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (524, 'W_BRANCH_TYPE', 'Kaelus', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (525, 'W_BRANCH_TYPE', 'Kolmik', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (526, 'W_BRANCH_TYPE', 'Nelik', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (527, 'W_BRANCH_TYPE', 'Liitmik', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (528, 'W_BRANCH_TYPE', 'Üleminek', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (529, 'W_BRANCH_TYPE', 'Äärik', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (530, 'W_BRANCH_TYPE', 'Sadul', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (531, 'W_BRANCH_TYPE', 'Otsakork', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (532, 'W_BRANCH_TYPE_SUB', 'Määramata', NULL, 'Liitmiku alamtüüp', NULL);
INSERT INTO evel.sn_constant VALUES (533, 'W_BRANCH_TYPE_SUB', 'T-kolmik muhviga', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (534, 'W_BRANCH_TYPE_SUB', 'T-kolmik flantsiga ', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (535, 'W_BRANCH_TYPE_SUB', 'elektrikeevisliitmik', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (536, 'W_DUCT_DIAMETER', '20', NULL, 'Veetoru diameeter', NULL);
INSERT INTO evel.sn_constant VALUES (537, 'W_DUCT_DIAMETER', '25', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (538, 'W_DUCT_DIAMETER', '32', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (539, 'W_DUCT_DIAMETER', '40', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (540, 'W_DUCT_DIAMETER', '50', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (541, 'W_DUCT_DIAMETER', '63', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (542, 'W_DUCT_DIAMETER', '90', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (543, 'W_DUCT_DIAMETER', '100', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (544, 'W_DUCT_DIAMETER', '110', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (545, 'W_DUCT_DIAMETER', '125', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (546, 'W_DUCT_DIAMETER', '150', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (547, 'W_DUCT_DIAMETER', '160', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (548, 'W_DUCT_DIAMETER', '180', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (549, 'W_DUCT_DIAMETER', '200', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (550, 'W_DUCT_DIAMETER', '225', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (551, 'W_DUCT_DIAMETER', '250', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (552, 'W_DUCT_DIAMETER', '300', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (553, 'W_DUCT_DIAMETER', '350', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (554, 'W_DUCT_DIAMETER', '400', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (555, 'W_DUCT_MATERIAL', 'Määramata', NULL, 'Veetoru materjal', NULL);
INSERT INTO evel.sn_constant VALUES (556, 'W_DUCT_MATERIAL', 'Malm', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (557, 'W_DUCT_MATERIAL', 'Teras', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (558, 'W_DUCT_MATERIAL', 'Sukk', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (559, 'W_DUCT_MATERIAL', 'PE', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (560, 'W_DUCT_MATERIAL', 'PVC', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (561, 'W_DUCT_MATERIAL', 'PE RC', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (562, 'W_MANHOLE_DIAMETER', '400', NULL, 'Veekaevu diameeter', NULL);
INSERT INTO evel.sn_constant VALUES (563, 'W_MANHOLE_DIAMETER', '560', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (564, 'W_MANHOLE_DIAMETER', '700', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (565, 'W_MANHOLE_DIAMETER', '1000', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (566, 'W_MANHOLE_DIAMETER', '1500', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (567, 'W_MANHOLE_DIAMETER', '2000', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (568, 'W_MANHOLE_DIAMETER', '2500', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (569, 'W_MANHOLE_DIAMETER', '3000', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (570, 'W_MANHOLE_TYPE', 'Määramata', NULL, 'Vee seadmekaev', NULL);
INSERT INTO evel.sn_constant VALUES (571, 'W_MANHOLE_TYPE', 'Arvestikaev', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (572, 'W_MANHOLE_TYPE', 'Hoolduskaev', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (573, 'W_MANHOLE_TYPE', 'Läbipesusõlm', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (574, 'W_OTHER_NODE_TYPE', 'Määramata', NULL, 'Vee muude punktobjektide tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (575, 'W_OTHER_NODE_TYPE', 'Kaitsearmatuur', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (576, 'W_OTHER_NODE_TYPE', 'Veetöötlusjaam', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (577, 'W_OTHER_NODE_TYPE_SUB', 'Määramata', NULL, 'Vee muude punktobjektide alamtüüp', NULL);
INSERT INTO evel.sn_constant VALUES (578, 'W_OTHER_NODE_TYPE_SUB', 'Õhueraldi', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (579, 'W_OTHER_NODE_TYPE_SUB', 'Tagasilöögiklapp', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (580, 'W_OTHER_NODE_TYPE_SUB', 'Ülerõhuklapp', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (581, 'W_PRESSURE_STATION_TYPE', 'Reguleerimissõlm', NULL, 'Reguleerimissõlme tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (582, 'W_PRESSURE_STATION_TYPE_SUB', 'Survetõste pumpla', NULL, 'Reguleerimissõlme alamtüüp', NULL);
INSERT INTO evel.sn_constant VALUES (583, 'W_PRESSURE_STATION_TYPE_SUB', 'Rõhu alandamine', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (584, 'W_PRESSURE_STATION_TYPE_SUB', 'Hüdrofoor', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (585, 'W_PUMP_TYPE', 'Määramata', NULL, 'Veepumba tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (586, 'W_TANK_TYPE', 'Määramata', NULL, 'Veemahuti tüüp', NULL);
INSERT INTO evel.sn_constant VALUES (587, 'W_TANK_TYPE', 'Veetorn', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (588, 'W_TANK_TYPE', 'Veepaak', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (589, 'W_VALVE_TYPE', 'Liini', NULL, 'Vee sulgeseadme liik', NULL);
INSERT INTO evel.sn_constant VALUES (590, 'W_VALVE_TYPE', 'Kinnistu', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (591, 'W_VALVE_TYPE_SUB', 'Määramata', NULL, 'Vee sulgeseadme alamliik', NULL);
INSERT INTO evel.sn_constant VALUES (592, 'W_VALVE_TYPE_SUB', 'Kiil', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (593, 'W_VALVE_TYPE_SUB', 'Klapp', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (594, 'W_VALVE_TYPE_SUB', 'Kummikiil', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (595, 'W_VALVE_TYPE_SUB', 'Kuulkraan', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (596, 'W_VALVE_TYPE_SUB', 'Korkkraan', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (597, 'W_VALVE_TYPE_SUB', 'Vene malm', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (598, 'VALVE_HAND', 'Määramata', NULL, 'Sulgeseadme käelisus', NULL);
INSERT INTO evel.sn_constant VALUES (599, 'VALVE_HAND', 'Parem', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (600, 'VALVE_HAND', 'Vasak', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (601, 'VOLTAGE', 'Määramata', NULL, 'Pinge', NULL);
INSERT INTO evel.sn_constant VALUES (602, 'VOLTAGE', '230', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (603, 'VOLTAGE', '400', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (604, 'VOLTAGE', '1000', NULL, NULL, NULL);
INSERT INTO evel.sn_constant VALUES (605, 'VOLTAGE', '5000', NULL, NULL, NULL);


--
-- TOC entry 9678 (class 2606 OID 6824427)
-- Name: sn_constant pk_sn_constant; Type: CONSTRAINT; Schema: evel; Owner: postgres
--

ALTER TABLE ONLY evel.sn_constant
    ADD CONSTRAINT pk_sn_constant PRIMARY KEY (id);


-- Completed on 2021-12-02 11:21:45

--
-- PostgreSQL database dump complete
--


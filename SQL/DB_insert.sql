
-- database name : PrepaPySql

delete from `class`;
insert into `class`
(id, `name`) values
(1, "feca"),
(2, "osamodas"),
(3, "enutrof"),
(4, "sram"),
(5, "xelor"),
(6, "ecaflip"),
(7, "eniripsa"),
(8, "iop"),
(9, "cra"),
(10, "sadida"),
(11, "sacrieur"),
(12, "pandawa"),
(13, "roublard"),
(14, "zobal"),
(15, "steamer"),
(16, "eliotrop"),
(17, "huppermage"),
(18, "ouginak"),
(19, "forgelance");

delete from `adventurer`;
insert into `adventurer`
(id, `name`, xp, lvl, class) values
(1, "Axolootl", 0, 1, 13);

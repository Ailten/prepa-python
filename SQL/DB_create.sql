
-- database name : PrepaPySql

create table if not exists `class` (
    `id` int(11) not null auto_increment,
    `name` varchar(16) not null
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;


create table if not exists `adventurer` (
    `id` int(11) not null auto_increment,
    `name` varchar(16) not null unique,
    `xp` int(11) not null default 0,
    `lvl` int(11) not null default 1,
    `idClass` int(11) not null,

    constraint `fk_class`
        foreign key (`idClass`)
        references `class`(`id`)
        on delete cascade
        on update cascade

    --KEY `fk_idClass` (`idClass`),
    --CONSTRAINT `fk_idClass` PRIMARY KEY (id) REFERENCES class(id)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;


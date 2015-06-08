#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

from dbconn import db_cursor

def create_db():
    sqlstr = """
    DROP TABLE IF EXISTS course;

    CREATE TABLE IF NOT EXISTS course  (
        cou_sn   INTEGER,     --序号
        cou_no   TEXT,        --课程号
        name     TEXT,        --课程名称
        notes    TEXT,
        PRIMARY KEY(cou_sn)
    );
    -- CREATE UNIQUE INDEX idx_course_no ON course(cou_no)创建唯一索引;

    CREATE SEQUENCE seq_cou_sn 
        START 10000 INCREMENT 1 OWNED BY course.cou_sn;

    """
    with db_cursor() as cur :
        cur.execute(sqlstr) # 执行SQL语句

def init_data():
    sqlstr = """
    DELETE FROM course;

    INSERT INTO course (cou_sn, cou_no, name)  VALUES 
        (101, 'C01',  '高数'), 
        (102, 'C02',  '外语'),
        (103, 'C03',  '线代');

    """
    with db_cursor() as cur :
        cur.execute(sqlstr)    

if __name__ == '__main__':
    create_db()
    init_data()
    print('数据库已初始化完毕！')


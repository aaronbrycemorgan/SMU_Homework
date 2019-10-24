{\rtf1\ansi\ansicpg1252\cocoartf2509
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 SELECT \
	e.emp_no,\
	e.last_name,\
	e.first_name,\
	dm.dept_no,\
	d.dept_name,\
	dm.from_date,\
	dm.to_date\
FROM\
	employees e\
JOIN dept_manager dm\
	ON e.emp_no = dm.emp_no\
JOIN departments d\
	ON dm.dept_no = d.dept_no\
ORDER BY\
	e.last_name ASC;}
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
	d.dept_name\
FROM\
	employees AS e\
JOIN dept_emp AS de\
	ON de.emp_no = e.emp_no\
JOIN departments AS d\
	ON d.dept_no = de.dept_no\
WHERE \
	d.dept_name = 'Sales'\
ORDER BY\
	e.last_name ASC;}
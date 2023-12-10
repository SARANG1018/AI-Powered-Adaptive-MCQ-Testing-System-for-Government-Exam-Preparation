--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Debian 15.4-1.pgdg120+1)
-- Dumped by pg_dump version 15.3

-- Started on 2023-12-09 22:22:21 IST

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

SET default_table_access_method = heap;

--
-- TOC entry 214 (class 1259 OID 16418)
-- Name: student; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student (
    student_id bigint NOT NULL,
    student_name text NOT NULL
);


ALTER TABLE public.student OWNER TO postgres;

--
-- TOC entry 3371 (class 0 OID 16418)
-- Dependencies: 214
-- Data for Name: student; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student (student_id, student_name) FROM stdin;
\.


--
-- TOC entry 3228 (class 2606 OID 16424)
-- Name: student student_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_pkey PRIMARY KEY (student_id);


-- Completed on 2023-12-09 22:22:21 IST

--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Debian 15.4-1.pgdg120+1)
-- Dumped by pg_dump version 15.3

-- Started on 2023-12-09 22:21:00 IST

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

SET default_table_access_method = heap;

--
-- TOC entry 216 (class 1259 OID 16432)
-- Name: level_of_education; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.level_of_education (
    level_of_education_id bigint NOT NULL,
    level_of_education_name text NOT NULL
);


ALTER TABLE public.level_of_education OWNER TO postgres;

--
-- TOC entry 3371 (class 0 OID 16432)
-- Dependencies: 216
-- Data for Name: level_of_education; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.level_of_education (level_of_education_id, level_of_education_name) FROM stdin;
\.


--
-- TOC entry 3228 (class 2606 OID 16438)
-- Name: level_of_education level_of_education_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.level_of_education
    ADD CONSTRAINT level_of_education_pkey PRIMARY KEY (level_of_education_id);


-- Completed on 2023-12-09 22:21:01 IST

--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Debian 15.4-1.pgdg120+1)
-- Dumped by pg_dump version 15.3

-- Started on 2023-12-09 22:17:49 IST

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

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16425)
-- Name: courses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.courses (
    courses_id bigint NOT NULL,
    courses_name text NOT NULL,
    level_id bigint
);


ALTER TABLE public.courses OWNER TO postgres;

--
-- TOC entry 3372 (class 0 OID 16425)
-- Dependencies: 215
-- Data for Name: courses; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.courses (courses_id, courses_name, level_id) FROM stdin;
\.


--
-- TOC entry 3228 (class 2606 OID 16431)
-- Name: courses courses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_pkey PRIMARY KEY (courses_id);


--
-- TOC entry 3229 (class 2606 OID 16439)
-- Name: courses courses_level_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_level_id_fkey FOREIGN KEY (level_id) REFERENCES public.level_of_education(level_of_education_id) NOT VALID;


-- Completed on 2023-12-09 22:17:50 IST

--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Debian 15.4-1.pgdg120+1)
-- Dumped by pg_dump version 15.3

-- Started on 2023-12-09 22:22:32 IST

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

SET default_table_access_method = heap;

--
-- TOC entry 217 (class 1259 OID 16444)
-- Name: student_courses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_courses (
    student_id bigint NOT NULL,
    course_id bigint NOT NULL
);


ALTER TABLE public.student_courses OWNER TO postgres;

--
-- TOC entry 3373 (class 0 OID 16444)
-- Dependencies: 217
-- Data for Name: student_courses; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_courses (student_id, course_id) FROM stdin;
\.


--
-- TOC entry 3228 (class 2606 OID 16448)
-- Name: student_courses student_courses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_courses
    ADD CONSTRAINT student_courses_pkey PRIMARY KEY (student_id, course_id);


--
-- TOC entry 3229 (class 2606 OID 16454)
-- Name: student_courses student_courses_course_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_courses
    ADD CONSTRAINT student_courses_course_id_fkey FOREIGN KEY (course_id) REFERENCES public.courses(courses_id) NOT VALID;


--
-- TOC entry 3230 (class 2606 OID 16449)
-- Name: student_courses student_courses_student_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_courses
    ADD CONSTRAINT student_courses_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.student(student_id) NOT VALID;


-- Completed on 2023-12-09 22:22:32 IST

--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Debian 15.4-1.pgdg120+1)
-- Dumped by pg_dump version 15.3

-- Started on 2023-12-09 22:22:43 IST

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

SET default_table_access_method = heap;

--
-- TOC entry 221 (class 1259 OID 16510)
-- Name: test; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.test (
    test_id bigint NOT NULL,
    student_id bigint,
    date date NOT NULL
);


ALTER TABLE public.test OWNER TO postgres;

--
-- TOC entry 3372 (class 0 OID 16510)
-- Dependencies: 221
-- Data for Name: test; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.test (test_id, student_id, date) FROM stdin;
\.


--
-- TOC entry 3228 (class 2606 OID 16514)
-- Name: test test_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test
    ADD CONSTRAINT test_pkey PRIMARY KEY (test_id);


--
-- TOC entry 3229 (class 2606 OID 16515)
-- Name: test test_student_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test
    ADD CONSTRAINT test_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.student(student_id) NOT VALID;


-- Completed on 2023-12-09 22:22:43 IST

--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Debian 15.4-1.pgdg120+1)
-- Dumped by pg_dump version 15.3

-- Started on 2023-12-09 22:22:09 IST

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

SET default_table_access_method = heap;

--
-- TOC entry 218 (class 1259 OID 16474)
-- Name: specilizations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.specilizations (
    specilization_id bigint NOT NULL,
    year_of_study date NOT NULL,
    specilization_name text NOT NULL,
    specilization_syllabus text,
    specilization_reference_books text,
    course_id bigint NOT NULL
);


ALTER TABLE public.specilizations OWNER TO postgres;

--
-- TOC entry 3372 (class 0 OID 16474)
-- Dependencies: 218
-- Data for Name: specilizations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.specilizations (specilization_id, year_of_study, specilization_name, specilization_syllabus, specilization_reference_books, course_id) FROM stdin;
\.


--
-- TOC entry 3228 (class 2606 OID 16480)
-- Name: specilizations specilizations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.specilizations
    ADD CONSTRAINT specilizations_pkey PRIMARY KEY (specilization_id);


--
-- TOC entry 3229 (class 2606 OID 16481)
-- Name: specilizations specilizations_course_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.specilizations
    ADD CONSTRAINT specilizations_course_id_fkey FOREIGN KEY (course_id) REFERENCES public.courses(courses_id) NOT VALID;


-- Completed on 2023-12-09 22:22:09 IST

--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Debian 15.4-1.pgdg120+1)
-- Dumped by pg_dump version 15.3

-- Started on 2023-12-09 22:21:40 IST

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

SET default_table_access_method = heap;

--
-- TOC entry 219 (class 1259 OID 16486)
-- Name: questions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.questions (
    question_id bigint NOT NULL,
    specilization_id bigint NOT NULL,
    question text NOT NULL,
    answer text NOT NULL
);


ALTER TABLE public.questions OWNER TO postgres;

--
-- TOC entry 3372 (class 0 OID 16486)
-- Dependencies: 219
-- Data for Name: questions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.questions (question_id, specilization_id, question, answer) FROM stdin;
\.


--
-- TOC entry 3228 (class 2606 OID 16492)
-- Name: questions questions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.questions
    ADD CONSTRAINT questions_pkey PRIMARY KEY (question_id);


--
-- TOC entry 3229 (class 2606 OID 16493)
-- Name: questions questions_specilization_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.questions
    ADD CONSTRAINT questions_specilization_id_fkey FOREIGN KEY (specilization_id) REFERENCES public.specilizations(specilization_id) NOT VALID;


-- Completed on 2023-12-09 22:21:40 IST

--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Debian 15.4-1.pgdg120+1)
-- Dumped by pg_dump version 15.3

-- Started on 2023-12-09 22:21:28 IST

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

SET default_table_access_method = heap;

--
-- TOC entry 220 (class 1259 OID 16498)
-- Name: question_options; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.question_options (
    question_option_id bigint NOT NULL,
    value text NOT NULL,
    question_id bigint
);


ALTER TABLE public.question_options OWNER TO postgres;

--
-- TOC entry 3372 (class 0 OID 16498)
-- Dependencies: 220
-- Data for Name: question_options; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.question_options (question_option_id, value, question_id) FROM stdin;
\.


--
-- TOC entry 3228 (class 2606 OID 16504)
-- Name: question_options question_options_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question_options
    ADD CONSTRAINT question_options_pkey PRIMARY KEY (question_option_id);


--
-- TOC entry 3229 (class 2606 OID 16505)
-- Name: question_options question_options_question_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question_options
    ADD CONSTRAINT question_options_question_id_fkey FOREIGN KEY (question_id) REFERENCES public.questions(question_id) NOT VALID;


-- Completed on 2023-12-09 22:21:29 IST

--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Debian 15.4-1.pgdg120+1)
-- Dumped by pg_dump version 15.3

-- Started on 2023-12-09 22:21:55 IST

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

SET default_table_access_method = heap;

--
-- TOC entry 222 (class 1259 OID 16520)
-- Name: specilization_test; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.specilization_test (
    test_id bigint NOT NULL,
    question_id bigint NOT NULL
);


ALTER TABLE public.specilization_test OWNER TO postgres;

--
-- TOC entry 3373 (class 0 OID 16520)
-- Dependencies: 222
-- Data for Name: specilization_test; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.specilization_test (test_id, question_id) FROM stdin;
\.


--
-- TOC entry 3228 (class 2606 OID 16524)
-- Name: specilization_test specilization_test_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.specilization_test
    ADD CONSTRAINT specilization_test_pkey PRIMARY KEY (question_id, test_id);


--
-- TOC entry 3229 (class 2606 OID 16530)
-- Name: specilization_test specilization_test_question_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.specilization_test
    ADD CONSTRAINT specilization_test_question_id_fkey FOREIGN KEY (question_id) REFERENCES public.questions(question_id) NOT VALID;


--
-- TOC entry 3230 (class 2606 OID 16525)
-- Name: specilization_test specilization_test_test_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.specilization_test
    ADD CONSTRAINT specilization_test_test_id_fkey FOREIGN KEY (test_id) REFERENCES public.test(test_id) NOT VALID;


-- Completed on 2023-12-09 22:21:56 IST

--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Debian 15.4-1.pgdg120+1)
-- Dumped by pg_dump version 15.3

-- Started on 2023-12-09 22:22:55 IST

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

SET default_table_access_method = heap;

--
-- TOC entry 223 (class 1259 OID 16535)
-- Name: test_questions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.test_questions (
    test_id bigint NOT NULL,
    question_id bigint NOT NULL
);


ALTER TABLE public.test_questions OWNER TO postgres;

--
-- TOC entry 3373 (class 0 OID 16535)
-- Dependencies: 223
-- Data for Name: test_questions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.test_questions (test_id, question_id) FROM stdin;
\.


--
-- TOC entry 3228 (class 2606 OID 16539)
-- Name: test_questions test_questions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test_questions
    ADD CONSTRAINT test_questions_pkey PRIMARY KEY (test_id, question_id);


--
-- TOC entry 3229 (class 2606 OID 16545)
-- Name: test_questions test_questions_question_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test_questions
    ADD CONSTRAINT test_questions_question_id_fkey FOREIGN KEY (question_id) REFERENCES public.questions(question_id) NOT VALID;


--
-- TOC entry 3230 (class 2606 OID 16540)
-- Name: test_questions test_questions_test_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test_questions
    ADD CONSTRAINT test_questions_test_id_fkey FOREIGN KEY (test_id) REFERENCES public.test(test_id) NOT VALID;


-- Completed on 2023-12-09 22:22:56 IST

--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Debian 15.4-1.pgdg120+1)
-- Dumped by pg_dump version 15.3

-- Started on 2023-12-09 22:21:15 IST

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

SET default_table_access_method = heap;

--
-- TOC entry 224 (class 1259 OID 16550)
-- Name: question_analytics; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.question_analytics (
    question_id bigint NOT NULL,
    total_attempts bigint DEFAULT 0 NOT NULL,
    total_correct bigint DEFAULT 0 NOT NULL,
    difficulty double precision NOT NULL
);


ALTER TABLE public.question_analytics OWNER TO postgres;

--
-- TOC entry 3374 (class 0 OID 16550)
-- Dependencies: 224
-- Data for Name: question_analytics; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.question_analytics (question_id, total_attempts, total_correct, difficulty) FROM stdin;
\.


--
-- TOC entry 3230 (class 2606 OID 16556)
-- Name: question_analytics question_analytics_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question_analytics
    ADD CONSTRAINT question_analytics_pkey PRIMARY KEY (question_id);


--
-- TOC entry 3231 (class 2606 OID 16557)
-- Name: question_analytics question_analytics_question_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question_analytics
    ADD CONSTRAINT question_analytics_question_id_fkey FOREIGN KEY (question_id) REFERENCES public.questions(question_id) NOT VALID;


-- Completed on 2023-12-09 22:21:15 IST

--
-- PostgreSQL database dump complete
--


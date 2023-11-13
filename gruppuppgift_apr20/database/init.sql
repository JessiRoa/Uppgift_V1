CREATE TABLE public.results (
    id SERIAL,
    original INT,
    saved TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    factors VARCHAR(1000)
);

INSERT INTO public.results 
    (original, factors, saved)
VALUES
    (2, '2', '2023-01-01'),
    (3, '3', '2023-01-01')
;

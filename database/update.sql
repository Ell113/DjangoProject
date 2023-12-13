CREATE or replace FUNCTION post_update() RETURNS trigger
AS $$
	DECLARE countFlight int;
    BEGIN
		if NEW.publish > current_date then
			return NULL;
		else 
			return NEW;
		end if;
	END;
$$ LANGUAGE plpgsql;

CREATE or replace TRIGGER tr_post_up
before UPDATE ON blog_post
FOR EACH row
EXECUTE FUNCTION post_update();

select * from blog_post

update blog_post set publish = '2023-12-11 21:28:14.435721+03' where title = 'not my post'
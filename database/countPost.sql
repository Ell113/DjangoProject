create or replace function countOfPost(idUs int, statusP text) returns int
as $$
declare countP int;
begin
	select count(*) into countP from blog_post where author_id = idUs and status = statusP;
	return countP;
end;$$ language plpgsql

function out = act2mat(proj_meta, x, tp)

out = vertcat(proj_meta(x).rd(1:size(proj_meta(x).rd,1), tp).act); 

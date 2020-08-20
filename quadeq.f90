program quadraticequation
  implicit none
  real a,b,c
  complex answer1,answer2,root
  write(*,*) "Enter the coefficients a,b,c of the polynomial"
  read(*,*) a,b,c
  
  root = b**2 - 4*a*c

  write(*,*) "roots: "

  if (root == 0) then
    write(*,*) -b / 2*a
  else
    answer1 = (-b + sqrt(root) )/ (2*a)
    answer2 = (-b - sqrt(root) )/ (2*a)
  endif

  if (real(root) > 0) then
    write(*,*) real(answer1), real(answer2)
  elseif (real(root) < 0) then
    write(*,*) answer1, answer2
  endif

end program

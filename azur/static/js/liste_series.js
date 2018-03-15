function hide_bottom(object)
{
    object.style.height='150px';
}

function reveal_bottom(object)
{
    var size2=object.getElementsByClassName("troisieme_bloc")[0].clientHeight;
    object.style.height=(150+size2)+'px';
}

var file_list=document.getElementsByClassName("element_conteneur");

for (var iter=0; iter<file_list.length; iter++)
{
    hide_bottom(file_list[iter]);
    (function(iter,file_list)
    {
        file_list[iter].addEventListener("mouseover",function() {reveal_bottom(file_list[iter])});
        file_list[iter].addEventListener("mouseout", function() {hide_bottom(file_list[iter])});
    })(iter,file_list)
}

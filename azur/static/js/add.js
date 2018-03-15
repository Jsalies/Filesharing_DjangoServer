function changedisplay()
{
    var formlist = ['films','series','jeux','logiciels','livres','musiques'];
    var choix = document.getElementById("choix").value;
    for(var i=0; i<6;i++)
    {
        if (formlist[i]==choix)
        {
            document.getElementById(formlist[i]).style.display="block";
        }
        else
        {
            document.getElementById(formlist[i]).style.display="none";
        }
    }
}
changedisplay()
document.getElementById("choix").addEventListener("change", changedisplay);

var choisi = document.getElementById("rappel_formulaire").innerHTML;

document.getElementById("choix").selectedIndex=choisi-1;
changedisplay()
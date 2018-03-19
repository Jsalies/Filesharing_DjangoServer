//agrandi l'image du menu ciblée
function menuIn(cible)
{
    if (window.innerWidth > 500)
    {
        var myArray = ['menu1', 'menu2', 'menu3', 'menu4', 'menu5', 'menu6'];
        for(var i=0; i<6;i++)
        {
            if (myArray[i]==cible)
            {
                document.getElementById(myArray[i]).style.marginRight="-4.4%";
            }
            else
            {
                document.getElementById(myArray[i]).style.marginRight="-10%";
            }
        }
    }
}

//Rétrecie l'ensemble des images
function menuOut(cible)
{
    var myArray = ['menu1', 'menu2', 'menu3', 'menu4', 'menu5', 'menu6'];
    for(var i=0; i<6;i++)
    {
        document.getElementById(myArray[i]).style.marginRight="-10%";
    }
}

function textSize()
{
    var hauteur = document.getElementById("menu1").clientHeight;
    hauteur = Math.round(0.7*hauteur);
    var font= Math.round(0.15*hauteur)
    var objets = document.getElementsByClassName('menu');
    for(var i=0; i<6;i++)
    {
        var span=objets[i].getElementsByTagName('span')[0];
        span.style.top=hauteur+"px";
        span.style.fontSize=font+"px";
    }
}

//ensemble des evenements pour agrandir les images

document.getElementById("menu1").addEventListener("mouseover", function() {menuIn("menu1")});
document.getElementById("menu2").addEventListener("mouseover", function() {menuIn("menu2")});
document.getElementById("menu3").addEventListener("mouseover", function() {menuIn("menu3")});
document.getElementById("menu4").addEventListener("mouseover", function() {menuIn("menu4")});
document.getElementById("menu5").addEventListener("mouseover", function() {menuIn("menu5")});
document.getElementById("menu6").addEventListener("mouseover", function() {menuIn("menu6")});

//ensemble des evenements pour retrecir les images
document.getElementById("menu1").addEventListener("mouseout", function() {menuOut()});
document.getElementById("menu2").addEventListener("mouseout", function() {menuOut()});
document.getElementById("menu3").addEventListener("mouseout", function() {menuOut()});
document.getElementById("menu4").addEventListener("mouseout", function() {menuOut()});
document.getElementById("menu5").addEventListener("mouseout", function() {menuOut()});
document.getElementById("menu6").addEventListener("mouseout", function() {menuOut()});

//evenement pour agrandir et replacer le texte du menu
textSize()
window.addEventListener('resize',textSize)
setTimeout(textSize,1000)


function addtransition()
{
    menu=document.getElementsByClassName("menu")
    for(var i=0; i<menu.length;i++)
    {
        menu[i].style.transition = "0.7s ease-in-out";
    }
    toolbar=document.getElementById("toolbarmenu").getElementsByTagName("DIV")
    for(var i=0; i<toolbar.length;i++)
    {
        toolbar[i].style.transition = "color 0.5s,background-position 1s";
    }
    
    toolbar2=document.getElementById("administration").getElementsByTagName("A");
    for(var i=0; i<toolbar2.length;i++)
    {
        toolbar2[i].style.transition = "color 0.5s";
    }
    
     toolbar3=document.getElementById("retour_accueil").getElementsByTagName("A");
    for(var i=0; i<toolbar3.length;i++)
    {
        toolbar3[i].style.transition = "color 0.5s";
    }
}

addtransition()

function setElementActive(element)
{
    $(".active").removeClass("active");
    $(element).addClass("active");
}
function setTitle(titleContainer, message)
{
    $(titleContainer).text(message);
}
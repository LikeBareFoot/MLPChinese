<script>
<!--
function toggleIdVisibility(id) {
  var e = document.getElementById(id);
  if(e.style.display == 'none')
    e.style.display = 'block';
  else
    e.style.display = 'none';
}

function toggleClassVisibility(className) {
    elements = document.getElementsByClassName(className);
    for (var i = 0; i < elements.length; i++) {
        elements[i].style.display = elements[i].style.display == 'none' ? 'block' : 'none';
    }
}

function toggleDisplay(element, className) {
    var curr = element.value;
    if(curr == 1){
        element.value = 0;
        element.innerText = "显示拼音";
        elements = document.getElementsByClassName(className);
        for (var i = 0; i < elements.length; i++) {
            elements[i].style.display = 'none';
        }
    } else {
        element.value = 1;
        element.innerText = "隐藏拼音";
        elements = document.getElementsByClassName(className);
        for (var i = 0; i < elements.length; i++) {
            elements[i].style.display = 'block';
        }
    }
}
-->
</script>

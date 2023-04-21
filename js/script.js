var nombre=document.getElementById('nombre');
var password=document.getElementById('password');
var error=document.getElementById('error');
error.style.color='red';
function enviarFormulario(){
    console.log('Enviando Formulario');
    var mensajesError=[];
    if(nombre.value === null||nombre.value ===''){
        mensajesError.push('Ingresa tu Nombre de Usuario');
    }
    if(password.value === null||password.value ===''){
        mensajesError.push('Ingresa tu Contraseña');
    }
    if(mensajesError.length>0){
        error.innerHTML=mensajesError.join(',');
        return false;
    }

   
}
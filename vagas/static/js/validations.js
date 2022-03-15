function icpf(v){
    v=v.replace(/\D/g,"")                    //Remove tudo o que nao e digito
    v=v.replace(/(\d{3})(\d)/,"$1.$2")       //Coloca um ponto entre o terceiro e o quarto digitos
    v=v.replace(/(\d{3})(\d)/,"$1.$2")       //Coloca um ponto entre o terceiro e o quarto digitos
                                            //de novo (para o segundo bloco de numeros)
    v=v.replace(/(\d{3})(\d{1,2})$/,"$1-$2") //Coloca um hifen entre o terceiro e o quarto digitos
    return v
}
function icnpj(v){
    v=v.replace(/\D/g,"")                    //Remove tudo o que nao e digito
    v=v.replace(/(\d{2})(\d)/,"$1.$2")       //Coloca um ponto entre o segundo e terceiro digitos
    v=v.replace(/(\d{3})(\d)/,"$1.$2")       //Coloca um ponto entre o quinto e o sexto digitos
    v=v.replace(/(\d{3})(\d)/,"$1/$2")       //Coloca um ponto entre o quinto e o sexto digitos
    v=v.replace(/(\d{4})(\d)/,"$1-$2")       //Coloca um ponto entre o quinto e o sexto digitos
    // v=v.replace(/^(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/, "$1.$2.$3/$4-$5")
    return v
}
function itelefone(v){
    v=v.replace(/\D/g,"")                 //Remove tudo o que nao e digito
    v=v.replace(/^(\d\d)(\d)/g,"($1) $2") //Coloca parenteses em volta dos dois primeiros digitos
    v=v.replace(/(\d{4})(\d)/,"$1-$2")    //Coloca hifen entre o quarto e o quinto digitos
    return v
}
function icep(v){
    v=v.replace(/\D/g,"")                 //Remove tudo o que nao e digito
    v=v.replace(/(\d{2})(\d)/,"$1.$2")    //Coloca hifen entre o quarto e o quinto digitos
    v=v.replace(/(\d{3})(\d)/,"$1-$2")    //Coloca hifen entre o quarto e o quinto digitos
    return v
}
function icelular(v){
    v=v.replace(/\D/g,"")                 //Remove tudo o que nao e digito
    v=v.replace(/^(\d\d)(\d)/g,"($1) $2") //Coloca parenteses em volta dos dois primeiros digitos
    v=v.replace(/(\d{5})(\d)/,"$1-$2")    //Coloca hifen entre o quarto e o quinto digitos
    return v
}
function mascara(o,f){
    v_obj=o
    v_fun=f
    setTimeout("execmascara()",1)
}

function execmascara(){
    v_obj.value=v_fun(v_obj.value)
}

function validar(event){
    event.target.classList.remove("is-invalid");
}
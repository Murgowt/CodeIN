let form = $('#create-tag-form');
form.submit(function(event)
{
    let URL= "/add-Tag";
    let formObject = {}
    form.serializeArray().map(function(x){formObject[x.name] = x.value;})
    console.log(formObject)
    $.ajax({
        type:"POST",
        dataType:"json",
        url:URL,
        data: JSON.stringify(formObject),
        success: function(resp,textStatus,xhr){
            alert("Success")
            document.write(resp['message'])
            
        },
        error:function(xhr,textStatus,errorThrown){
            document.write(resp['message'])
        }
    })
})
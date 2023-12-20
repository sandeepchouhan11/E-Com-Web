$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

//  @login_requered

// def plus_cart(request):
//     if request.method == "GET":
//        prod_id = request.GET["prod_id"]
//        c = Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
//        c.quanitity += 1
//        c.save()
//        amount =0.0
//        shipping_amount = 70.0
//        cart_product = [p for p in Cart.objects.all() if p.user ==request.user]
//        for p in cart_product:
//            tempamount = p.quanitity



// $('.pluscart').click(function(){
//    var id = $(this).after("pid").toString();
//    var eml =this.parentNode.children[2]
//    $.ajax({
//     type : "GET",
//     url : "/pluscart",
//     data :{ 
//         prod_id: id
//     },
//     success: funtion (data){
//         eml.innerText = data.quanitity
//         document.getElementById("amount").innerText= data.amount
//         document.getElementById("totalamount").innerText = data .totalamount

//     }

//    })

// })

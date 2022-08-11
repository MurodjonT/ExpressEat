console.log('Ishlayabdi')


// menu.htmlda add cart bo'lmiga datalarini yozish kerak



// mahsulotni id sini olish uchun js kodlaridan foydalanamiz
// var updateBtns = document.getElementsByClassName('update-cart')

// for(var i = 0; i < updateBtns.length; i++){
// 	updateBtns[i].addEventListener('click',function(){
// 		var productId = this.dataset.product
// 		var action = this.dataset.action
// 		console.log('productId:',productId,"action:",action)
// })
// }


// 6-bosqich
// Add cart bosilsa uni qaysi nuser bosyabdi shu ma'lumotni olishimiz uchun js kodlaridan foydalanamiz
// base.htmlga js kodlarini yozib kelishimiz kerak

var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
	updateBtns[i].addEventListener('click',function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:',productId,"action:",action)

		console.log('User:', user)
		if(user == 'AnonymousUser'){
			console.log('Not logging in')
		}else{
			updateUserOrder(productId, action)
		}
	})
}


// 7-bosqich 
// js yordamida Backendga POST yuborish uchun Token olishimiz kerak
// function updateUserOrder(productId, action) {
// 	console.log('User is liggin')

// 	var url = '/update_item/'
// 	fetch(url, {
// 		method: 'POST',
// 		headers: {
// 			'Content-Type': 'application/json',
			
// 		},
// 		body:JSON.stringify({'productId': productId,'action':action})
// 	})
// 	.then((response) =>{
// 		return response.json()
// 	})
// 	.then((data) =>{
// 		console.log('data:', data)
// 		location.reload()
// 	})
// }




// keygi uzgarish
function updateUserOrder(productId, action) {
	console.log('User is liggin')

	var url = '/update_item/'
	fetch(url, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken':csrftoken,
		},
		body:JSON.stringify({'productId': productId,'action':action})
	})
	.then((response) =>{
		return response.json()
	})
	.then((data) =>{
		console.log('data:', data)
		location.reload()
	})
}


// 8-bosqich
// views.py da funksiya xosil qilamiz
// base.htmlda js kodlarini yozishimiz kerak bo'ladi token olishimiz uchun

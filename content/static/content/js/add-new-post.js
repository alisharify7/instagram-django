function create_obj_uri(obj){
    return URL.createObjectURL(obj);
}

function create_owl_slider_child(images){ // create owl item div with given uri
    let d = [];
    Object.keys(images).forEach(each =>{
        if (each === "length"){
            return
        }
        let div = document.createElement("div");
        let image = document.createElement("img");
        div.className = "item w-100 h-100";
        image.src = images[each].uri;
        image.className = "img-fluid";
        div.appendChild(image);
        d.push(div)
    })
    return d;
}


const post_media_preloader = document.querySelector("#post-media-preloader");
 post_media_preloader.addEventListener('change', (media_input_event)=> {
   if (media_input_event.target.files.length <= 0) {
    media_input_event.preventDefault();
    return null;
   }
   const media_list = {};
   media_list["length"] = media_input_event.target.files.length;
   for(let i =0; i< media_input_event.target.files.length; i++){
       file = media_input_event.target.files[i];
           size = ((file.size / 1024) / 1024).toFixed(2)
           name = file.name
           type = file.type
           // validate file size:TODO
           media_list[name] = {type:type, size:size, obj: file, uri: create_obj_uri(file)};
   }
    // close modal
       document.querySelector("#add-new-post-preloader > div > div > div.modal-header.bg-brand-dark-50.border-0.px-5.pb-5.justify-content-center.align-items-center > button").click();
    // show post details modal
     const post_media_modal = document.querySelector("#add-new-post");
     const post_media_modal_handler = new bootstrap.Modal(post_media_modal, {})
     post_media_modal_handler.show()
     const post_image_slider_container = document.querySelector("#post-media-slider-container");

     create_owl_slider_child(media_list).forEach(div=>{
         // create owl items and add it to container
         post_image_slider_container.appendChild(div);
     })

      $("#post-media-slider-container").owlCarousel({
            rtl: true,
            loop: true,
            margin: 10,
            autoplay: true,
            responsiveClass: true,
            autoplayTimeout: 2000,
            autoplayHoverPause: true,
            lazyContent: true,
            lazyLoad: true,
            center: true,
            nav: true,
            responsive: {
                0: {
                    items: 1,
                },
            },
        });

 });




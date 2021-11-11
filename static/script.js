function searchToggle(obj, evt) {
    var container = $(obj).closest('.search-wrapper');
    if (!container.hasClass('active')) {
        container.addClass('active');
        //evt.preventDefault();            
    }
    else if (container.hasClass('active') && $(obj).closest('.input-holder').length == 0) {
        container.removeClass('active');
        // clear input
        container.find('.search-input').val('');
    }
    else {

    }
}
window.onload = function () { // window.addEventListener('load', (event) => {와 동일합니다.

    searchToggle($("#btn1"))
};
const form = document.querySelector('#form');


//hint: hold shift while opening to keep more than 1 open
let ds = [...document.querySelectorAll("details")];
ds.forEach((d) =>
    d.addEventListener(
        "click",
        (e) =>
            e.shiftKey ||
            ds.filter((i) => i != d).forEach((i) => i.removeAttribute("open"))
    )
);


form.addEventListener('submit', (e) => {
    console.log("들어왔냐")
    document.getElementById('loadingContainer').style.display = 'block';
    document.getElementById('loadingContainerGif').style.display = 'block';

});

function addReview_compare(data,rangePos)
{
    let reveiwCountNoraml = [0,0,0,0,0,0,0,0,0,0]
    let reveiwCount= [0,0,0,0,0,0,0,0,0,0]
    let posIndex

    
    for(i =0; i<data.length;i++)
    {        
        
        if (data[i][1] >= 90) {
            posIndex =9
            strType = '#page90'
        }
        else if (data[i][1] >= 80) {
            posIndex =8
            strType = '#page80'
        }
        else if (data[i][1] >= 70) {
            posIndex =7
            strType = '#page70'
        }
        else if (data[i][1] >= 60) {
            posIndex =6
            strType = '#page60'
        }
        else if (data[i][1] >= 50) {
            posIndex =5
            strType = '#page50'
        }
        else if (data[i][1] >= 40) {
            posIndex =4
            strType = '#page40'
        }
        else if (data[i][1] >= 30) {
            posIndex =3
            strType = '#page30'
        }
        else if (data[i][1] >= 20) {
            posIndex =2
            strType = '#page20'
        }
        else if (data[i][1] >= 10) {
            posIndex =1
            strType = '#page10'
        }
        else {
            posIndex =0
            strType = '#page00'
        }
        var value = data[i][1]
        let type = data[i][2]
        let review = data[i][0]
        let className = 'success'
        if(data[i][3] ==1)
        {
            
            className = 'failure'
            var template = `<li>
            <div class="${className}">
            ${review}
            <span class="type">
            ${type}
            </span>
            <span class="info">
            ${value}
            </span></div></li>`
            
            reveiwCount[posIndex] +=1
            $(strType).append(template)
        }                        
        
    }   

    
    for(i =0; i<data.length;i++)
    {        
        
        strPageClass = 'pageClass90'
        if (data[i][1] >= 90) {
            posIndex =9
            strType = '#page90'
            strPageClass = 'pageClass90'
        }
        else if (data[i][1] >= 80) {
            posIndex =8
            strType = '#page80'
            strPageClass = 'pageClass80'
        }
        else if (data[i][1] >= 70) {
            posIndex =7
            strType = '#page70'
            strPageClass = 'pageClass70'
        }
        else if (data[i][1] >= 60) {
            posIndex =6
            strType = '#page60'
            strPageClass = 'pageClass60'
        }
        else if (data[i][1] >= 50) {
            posIndex =5
            strType = '#page50'
            strPageClass = 'pageClass50'
        }
        else if (data[i][1] >= 40) {
            posIndex = 4
            strType = '#page40'
            strPageClass = 'pageClass40'
        }
        else if (data[i][1] >= 30) {
            posIndex = 3
            strType = '#page30'
            strPageClass = 'pageClass30'
        }
        else if (data[i][1] >= 20) {
            posIndex = 2
            strType = '#page20'
            strPageClass = 'pageClass20'
        }
        else if (data[i][1] >= 10) {
            posIndex = 1
            strType = '#page10'
            strPageClass = 'pageClass10'
        }
        else {
            posIndex =0
            strType = '#page00'
            strPageClass = 'pageClass00'
        }
        var value = data[i][1]
        let type = data[i][2]
        let review = data[i][0]
        let className = 'success'
        if(data[i][3] ==0)
        {
            
            className = 'success'
            var template = `<li>
            <div class="${className}">
            ${review}
            <span class="type">
            ${type}
            </span>
            <span class="info">
            ${value}
            </span></div></li>`
            
            reveiwCountNoraml[posIndex]+=1
            $(strType).append(template)
        }                     
        //console.log(reveiwCountNoraml)
        //console.log(reveiwCount)
        if(reveiwCount[posIndex]/(reveiwCount[posIndex]+reveiwCountNoraml[posIndex]) > 0.2)  
        {
            if(rangePos > posIndex*10)
            {
                document.getElementById(strPageClass).className = "warning"         
                document.getElementById(strPageClass).innerHTML = posIndex*10 +" % ↑ ( "+reveiwCount[posIndex] +" / "+reveiwCountNoraml[posIndex]+" ) "
                + " 합계 = " +(reveiwCount[posIndex]+reveiwCountNoraml[posIndex])
                +"  오차 "+Math.floor(reveiwCount[posIndex]/(reveiwCount[posIndex]+reveiwCountNoraml[posIndex]) *100)+" %" 
                +"   -일반 후기";
            }
            else{
                document.getElementById(strPageClass).className = "warning"         
                document.getElementById(strPageClass).innerHTML = posIndex*10 +" % ↑ ( "+reveiwCount[posIndex] +" / "+reveiwCountNoraml[posIndex]+" ) "
                + " 합계 = " +(reveiwCount[posIndex]+reveiwCountNoraml[posIndex])
                +"  오차 "+Math.floor(reveiwCount[posIndex]/(reveiwCount[posIndex]+reveiwCountNoraml[posIndex]) *100)+" %"
                +"   -불만 후기";
            }
         
        }
        else{
            if(rangePos > posIndex*10)
            {
                document.getElementById(strPageClass).className = "success"         
                    document.getElementById(strPageClass).innerHTML = posIndex*10 +" % ↑ ( "+reveiwCount[posIndex] +" / "+reveiwCountNoraml[posIndex]+" )"
                    + " 합계 = " +(reveiwCount[posIndex]+reveiwCountNoraml[posIndex])
                    +"  오차 "+Math.floor(reveiwCount[posIndex]/(reveiwCount[posIndex]+reveiwCountNoraml[posIndex]) *100)+" %"
                    +"   -일반 후기";    
            }
            else{
                document.getElementById(strPageClass).className = "success"         
                document.getElementById(strPageClass).innerHTML = posIndex*10 +" % ↑ ( "+reveiwCount[posIndex] +" / "+reveiwCountNoraml[posIndex]+" )"
                + " 합계 = " +(reveiwCount[posIndex]+reveiwCountNoraml[posIndex])
                +"  오차 "+Math.floor(reveiwCount[posIndex]/(reveiwCount[posIndex]+reveiwCountNoraml[posIndex]) *100)+" %"
                +"   -불만 후기";
            }
            
        }
    }   
    totalReview=0
    totalNoraml =0
    totalNotNormal =0
    for(i =0; i< reveiwCount.length;i++)
    {
        totalReview +=reveiwCount[i]
        totalNotNormal +=reveiwCount[i]
        totalNoraml +=reveiwCountNoraml[i]
        totalReview +=reveiwCountNoraml[i]
    }
    document.getElementById('infoTitle').innerHTML = "ROCKET GRAB"+"      합계 = "+totalReview
    +" ( "+totalNotNormal +" / "+ totalNoraml +" )" + "   오차 "+Math.floor(totalNotNormal/(totalReview)*100)+" %"

    //document.getElementById('pageClass90').className = "success"   
    //warning
    //ROCKET GRAB
    SetPage() 
}
function SetPage()
{
    $('#page90').paginate({
        perPage: 30,
        autoScroll: true,
        scope: '',
        paginatePosition: ['bottom'],
        useHashLocation: true,
        onPageClick: function () { }
    });
    $('#page80').paginate({
        perPage: 30,
        autoScroll: true,
        scope: '',
        paginatePosition: ['bottom'],
        useHashLocation: true,
        onPageClick: function () { }
      });
      $('#page70').paginate({
        perPage: 30,
        autoScroll: true,
        scope: '',
        paginatePosition: ['bottom'],
        useHashLocation: true,
        onPageClick: function () { }
      });
      $('#page60').paginate({
        perPage: 30,
        autoScroll: true,
        scope: '',
        paginatePosition: ['bottom'],
        useHashLocation: true,
        onPageClick: function () { }
      });
      $('#page50').paginate({
        perPage: 30,
        autoScroll: true,
        scope: '',
        paginatePosition: ['bottom'],
        useHashLocation: true,
        onPageClick: function () { }
      });
      $('#page40').paginate({
        perPage: 30,
        autoScroll: true,
        scope: '',
        paginatePosition: ['bottom'],
        useHashLocation: true,
        onPageClick: function () { }
      });
      $('#page30').paginate({
        perPage: 30,
        autoScroll: true,
        scope: '',
        paginatePosition: ['bottom'],
        useHashLocation: true,
        onPageClick: function () { }
      });
      $('#page20').paginate({
        perPage: 30,
        autoScroll: true,
        scope: '',
        paginatePosition: ['bottom'],
        useHashLocation: true,
        onPageClick: function () { }
      });
      $('#page10').paginate({
        perPage: 30,
        autoScroll: true,
        scope: '',
        paginatePosition: ['bottom'],
        useHashLocation: true,
        onPageClick: function () { }
      });
      $('#page00').paginate({
        perPage: 30,
        autoScroll: true,
        scope: '',
        paginatePosition: ['bottom'],
        useHashLocation: true,
        onPageClick: function () { }
      });
    
}
function addList(count, pos, review) {
    cnt = 1
    strType = '#type' + pos
    for (step = 0; step < count; step++) {
        var template = '<ul><li><label for="tall-1"><div class="ball" data-id="' + cnt + '"></div><p>' + review + '</p></div></label></li></ul>'

        $(strType).append(template)
        cnt++
    }

}
Data_review = []


function addReview(reviewData, count) {
    data = reviewData.replace(/\'/gi, "")
    //Data_review = data
    
    for (i = 0; i <= count - 1; i++) {

        arr = data.split(",")
        //console.log(arr)
        var regExp = /[ \{\}\[\]\/?.,;:|\)*~`!^\-_+┼<>@\#$%&\ '\"\\(\=]/gi;

        arr[i * 3] = arr[i * 3].replace(regExp, "")
        arr[i * 3] = arr[i * 3].replace(/[0-9]/g, ""); // 숫자제거

        arr[(i * 3) + 2] = arr[(i * 3) + 2].replace(regExp, "")
        arr[(i * 3) + 2] = arr[(i * 3) + 2].replace(/[0-9]/g, ""); // 숫자제거

        arr[(i * 3) + 1] = arr[(i * 3) + 1].replace(regExp, "")

        //console.log(arr[0])
        Data_review.push([arr[i * 3], arr[(i * 3) + 2], arr[(i * 3) + 1]])
    }

    console.log(Data_review)
    cnt = 1


    for (step = 0; step < Data_review.length; step++) {
        if (Data_review[step][2] >= 90)
            strType = '#type' + 1
        else if (Data_review[step][2] >= 80) {
            strType = '#type' + 2
        }
        else if (Data_review[step][2] >= 80) {
            strType = '#type' + 2
        }
        else if (Data_review[step][2] >= 70) {
            strType = '#type' + 3
        }
        else if (Data_review[step][2] >= 60) {
            strType = '#type' + 4
        }
        else if (Data_review[step][2] >= 50) {
            strType = '#type' + 5
        }
        else if (Data_review[step][2] >= 40) {
            strType = '#type' + 6
        }
        else if (Data_review[step][2] >= 30) {
            strType = '#type' + 7
        }
        else if (Data_review[step][2] >= 20) {
            strType = '#type' + 8
        }
        else if (Data_review[step][2] >= 10) {
            strType = '#type' + 9
        }
        else {
            strType = '#type' + 10
        }
        var template = '<ul><li><label for="tall-1"><div class="ball" data-id="' + cnt + '"></div><p>' + Data_review[step] + '</p></div></label></li></ul>'

        $(strType).append(template)
        cnt++
    }
    document.getElementById('loadingContainer').style.display = 'none';
    document.getElementById('loadingContainerGif').style.display = 'none';
}


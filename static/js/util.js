/**
 * Created with PyCharm.
 * User: stone
 * Date: 12-12-10
 * Time: 下午3:06
 * To change this template use File | Settings | File Templates.
 */
function changevalCityIns(targetObj,parentid,selectedid)
{
    var newoptsarr=new Array();
    var newoptsarrval=new Array();
    var newoptionI=0;
    //清除现有
    count1=targetObj.options.length;
    while(count1!=0)
    {
        targetObj.options.remove(0);
        count1=targetObj.options.length;
    }
    //过滤上级id=选中id
    for(var i=0;i<arrayCity.length;i++)
    {
        if(arrayCity[i][2]==parentid)
        {
            newoptsarr[newoptionI]=arrayCity[i][0];
            newoptsarrval[newoptionI]=arrayCity[i][3];
            var aOption = new Option(arrayCity[i][3],arrayCity[i][0]);
            targetObj.options[newoptionI]=aOption;
            if(arrayCity[i][0]==selectedid)
            {
                targetObj.options[newoptionI].selected=true;
            }
            newoptionI++;
        }
    }
    if(targetObj.id=="sheng")
    {
        changevalCityIns(document.getElementById("shi"),newoptsarr[0],0)
    }
    if(targetObj.id=="shi")
    {
        changevalCityIns(document.getElementById("xian"),newoptsarr[0],0)
    }
}

function changevalCityPls(targetObj,parentid,selectedid)
{
    var newoptsarr=new Array();
    var newoptsarrval=new Array();
    var newoptionI=0;
    //清除现有
    count1=targetObj.options.length;
    while(count1!=0)
    {
        targetObj.options.remove(0);
        count1=targetObj.options.length;
    }
    //过滤上级id=选中id
    for(var i=0;i<arrayCity.length;i++)
    {
        if(arrayCity[i][2]==parentid)
        {
            newoptsarr[newoptionI]=arrayCity[i][0];
            newoptsarrval[newoptionI]=arrayCity[i][3];
            var aOption = new Option(arrayCity[i][3],arrayCity[i][0]);
            targetObj.options[newoptionI]=aOption;
            if(arrayCity[i][0]==selectedid)
            {
                targetObj.options[newoptionI].selected=true;
            }
            newoptionI++;
        }
    }
    if(targetObj.id=="idPOLICYHOLDER_sheng")
    {
        changevalCityPls(document.getElementById("idPOLICYHOLDER_shi"),newoptsarr[0],0)
    }
    if(targetObj.id=="idPOLICYHOLDER_shi")
    {
        changevalCityPls(document.getElementById("idPOLICYHOLDER_xian"),newoptsarr[0],0)
    }
}




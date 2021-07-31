$(document).ready(function(){
	
	// Product Filter Start
	$(".filter-checkbox,#priceFilterBtn,#sortby").on('click',function(){
		var _filterObj={};
		var _minPrice=$('#maxPrice').attr('min');
		var _maxPrice=$('#maxPrice').val();
		var _sortprice=$('#sortby').val(); 
		console.log(_minPrice);
		console.log(_maxPrice);
		console.log(_sortprice);
		
		
		_filterObj.minPrice=_minPrice;
		_filterObj.maxPrice=_maxPrice;
		_filterObj.sortprice=_sortprice;
		$(".filter-checkbox").each(function(index,ele){
			var _filterVal=$(this).val();
			var _filterKey=$(this).data('filter');
			_filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
			 	return el.value;
			});
		});

		// Run Ajax
		$.ajax({
			url:'/filter-data',
			data:_filterObj,
			dataType:'json',
			beforeSend:function(){
				$("#filteredProducts").html('Loading data');
			},
			success:function(res){
				console.log(res);
				console.log("hii");
				$("#filteredProducts").html(res.data);
				
			}
			
		});
	});
	// End

	// Filter Product According to the price
	$("#maxPrice").on('blur',function(){
		var _min=$(this).attr('min');
		var _max=$(this).attr('max');
		var _value=$(this).val();
		console.log(_value,_min,_max);
		if(_value < parseInt(_min) || _value > parseInt(_max)){
			alert('Values should be '+_min+'-'+_max);
			$(this).val(_min);
			$(this).focus();
			$("#rangeInput").val(_min);
			return false;
		}
	});
	// End
});
$(document).ready(function () {

  $('form table tbody tr').formset({
    deleteText: '<i class="glyphicon glyphicon-trash"></i>',
    deleteCssClass: 'btn btn-sm btn-danger btn-formset btn-eliminar',
    addText: '<i class="glyphicon glyphicon-plus"></i> Add new item',
    addCssClass: 'btn btn-success',
    prefix: 'items'
  });

});
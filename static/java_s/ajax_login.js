$(document).ready(function () { 
    var status = $('#quicklogin-status').val(); 
    if (status == '1') { 
        ptlogin.changeEvent(); 
    } 
}); 
$(document).ajaxComplete(function () { 
    var status = $('#quicklogin-status').val(); 
    if (status == '1') { 
        ptlogin.changeEvent(); 
    } 
}); 
var ptlogin = {
    'loginAction': function (email, password) {
        $.ajax({
            url: 'index.php?route=plaza/login/login', type: 'post', data: { email: email, password: password }, dataType: 'json', beforeSend: function () { $('.ajax-load-img').show(); }, success: function (json) {
                if (json['success'] == true) {
                    if (json['enable_redirect']) { location = json['redirect']; } else { $('.pt-account').load('index.php?route=plaza/login/headerHtml #top-links ul.pt-account li'); $('#wishlist-total span').html(json['wishlist_total']); $('#wishlist-total').attr('title', json['wishlist_total']); $('#cart-total').html(json['cart_total']); $('#cart > ul').load('index.php?route=common/cart/info ul li'); $('body').before('<div class="alert alert-success"><i class="fa fa-check-circle"></i> ' + json['success_message'] + '<button type="button" class="close" data-dismiss="alert">&times;</button></div>'); }
                    ptlogin.closeForm(); $('.ajax-load-img').hide(); $('.login-form-content .alert-danger').remove();
                } else { $('.ajax-load-img').hide(); $('.login-form-content .alert-danger').remove(); $('#input-email').val(''); $('#input-password').val(''); $('.ajax-content .login-form-content').append('<div class="alert alert-danger"><i class="fa fa-exclamation-circle"></i> ' + json['error_warning'] + '<button type="button" class="close" data-dismiss="alert">&times;</button></div>'); }
            }
        });
    }, 'registerAction': function () {
        $('.for-error').removeClass('text-danger').hide(); $('.form-group').removeClass('has-error'); $.ajax({
            url: 'index.php?route=plaza/register/register', type: 'post', data: $('#ajax-register-form').serialize(), dataType: 'json', beforeSend: function () { $('.ajax-load-img').show(); }, success: function (json) {
                $('.ajax-load-img').hide(); if (json['success'] == true) { ptlogin.appendSuccess(); } else {
                    if (json['error_warning'] != '') { $('.error-warning span').html(" " + json['error_warning']); $('.error-warning').show(); }
                    if (json['error_firstname'] != '') { $('.error-firstname').addClass('text-danger').html(json['error_firstname']).show(); }
                    if (json['error_lastname'] != '') { $('.error-lastname').addClass('text-danger').html(json['error_lastname']).show(); }
                    if (json['error_email'] != '') { $('.error-email').addClass('text-danger').html(json['error_email']).show(); }
                    if (json['error_telephone'] != '') { $('.error-telephone').addClass('text-danger').html(json['error_telephone']).show(); }
                    if (json['error_custom_field'] != '') { $('.error-custom').addClass('text-danger').html(json['error_custom_field']).show(); }
                    if (json['error_password'] != '') { $('.error-password').addClass('text-danger').html(json['error_password']).show(); }
                    if (json['error_confirm'] != '') { $('.error-confirm').addClass('text-danger').html(json['error_confirm']).show(); }
                    $('.text-danger').each(function () { var element = $(this).parent().parent(); if (element.hasClass('form-group')) { element.addClass('has-error'); } });
                }
            }
        });
    }, 'logoutAction': function () {
        $.ajax({
            url: 'index.php?route=plaza/login/logout', dataType: 'json', beforeSend: function () { $('#ajax-login-block').show(); $('#ajax-loader').show(); }, success: function (json) {
                if (json['enable_redirect']) { location = json['redirect']; } else { $('.pt-account').load('index.php?route=plaza/login/headerHtml #top-links ul.pt-account li'); $('#wishlist-total span').html(json['wishlist_total']); $('#wishlist-total').attr('title', json['wishlist_total']); $('#cart-total').html(json['cart_total']); $('#cart > ul').load('index.php?route=common/cart/info ul li'); }
                $('#ajax-loader').hide(); ptlogin.appendLogoutSuccess();
            }
        });
    }, 'appendLoginForm': function () { ptlogin.resetLoginForm(); ptlogin.resetRegisterForm(); $('.ajax-body-login').show(); $('.account-register').hide('400'); $('#ajax-login-block').show(); $('.account-login').show('600'); }, 'appendRegisterForm': function () { ptlogin.resetLoginForm(); ptlogin.resetRegisterForm(); $('.ajax-body-login').show(); $('.account-login').hide('400'); $('#ajax-login-block').show(); $('.account-register').show('600'); }, 'appendSuccess': function () { $('.ajax-body-login').show(); $('.account-register').hide('400'); $('.account-success').show('600'); }, 'appendLogoutSuccess': function () { $('.ajax-body-login').show(); $('.logout-success').show('600'); }, 'resetLoginForm': function () { $('.login-form-content .alert-danger').remove(); $('#ajax-login-form')[0].reset(); }, 'resetRegisterForm': function () { $('.for-error').removeClass('text-danger').hide(); $('.form-group').removeClass('has-error'); $('#ajax-register-form')[0].reset(); }, 'closeForm': function () { $('#ajax-login-block').hide(); $('#ajax-loader').hide(); $('.account-login').hide('400'); $('.account-register').hide('400'); $('.account-success').hide(); $('.logout-success').hide(); $('.ajax-body-login').hide(); ptlogin.resetLoginForm(); ptlogin.resetRegisterForm(); }, 'changeEvent': function () { $('#pt-register-link').attr('href', 'javascript:void(0);').attr('onclick', 'ptlogin.appendRegisterForm()'); $('#pt-login-link').attr('href', 'javascript:void(0);').attr('onclick', 'ptlogin.appendLoginForm()'); $('#pt-logout-link').attr('href', 'javascript:void(0);').attr('onclick', 'ptlogin.logoutAction()'); }
};
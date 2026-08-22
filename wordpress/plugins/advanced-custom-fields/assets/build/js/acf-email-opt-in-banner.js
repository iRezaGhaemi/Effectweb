/******/ (() => { // webpackBootstrap
/*!*********************************************************************************!*\
  !*** ./src/advanced-custom-fields-pro/assets/src/js/acf-email-opt-in-banner.js ***!
  \*********************************************************************************/
/* global acf, acf_email_opt_in_banner */
(function ($) {
  $(function () {
    const $wrap = $('#acf-email-opt-in-banner-wrap');
    if (!$wrap.length) {
      return;
    }

    // Banner is rendered in the admin footer; move it into position above the table.
    const $wrapContent = $('#wpbody-content .wrap');
    const $postsFilter = $wrapContent.find('#posts-filter').first();
    const $searchBox = $postsFilter.find('.search-box').first();
    const $tablenavTop = $postsFilter.find('.tablenav.top').first();
    const $hr = $wrapContent.find('hr.wp-header-end').first();
    if ($tablenavTop.length) {
      $tablenavTop.before($wrap);
    } else if ($searchBox.length) {
      $searchBox.after($wrap);
    } else if ($postsFilter.length) {
      $postsFilter.prepend($wrap);
    } else if ($hr.length) {
      $hr.after($wrap);
    } else {
      $wrapContent.prepend($wrap);
    }
    $wrap.show();
    const $banner = $wrap.find('.acf-email-opt-in-banner');
    const $form = $banner.find('.acf-email-opt-in-banner__form');
    const $input = $banner.find('.acf-email-opt-in-banner__input');
    const $submit = $banner.find('.acf-email-opt-in-banner__submit');
    const $error = $banner.find('.acf-email-opt-in-banner__error');
    const $errorText = $banner.find('.acf-email-opt-in-banner__error-text');
    const $success = $banner.find('.acf-email-opt-in-banner__success');
    const $dismiss = $banner.find('.acf-email-opt-in-banner__dismiss');
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    function clearError() {
      $error.attr('hidden', true);
      $errorText.text('');
      $input.attr('aria-invalid', 'false');
    }
    function showError(message) {
      $errorText.text(message);
      $error.removeAttr('hidden');
      $input.attr('aria-invalid', 'true');
    }
    function setSubmitting(isSubmitting) {
      if (isSubmitting) {
        $submit.attr('disabled', 'disabled');
        $submit.attr('aria-busy', 'true');
      } else {
        $submit.removeAttr('disabled');
        $submit.removeAttr('aria-busy');
      }
    }
    function showSuccess() {
      clearError();
      $form.attr('hidden', true);
      $success.removeAttr('hidden');
    }
    function persistState(state) {
      $.ajax({
        url: acf.get('ajaxurl'),
        data: acf.prepareForAjax({
          action: 'acf/email_opt_in_banner/state',
          state: state
        }),
        type: 'post',
        dataType: 'json'
      });
    }
    function submitOptIn(email) {
      return $.ajax({
        url: acf.get('ajaxurl'),
        data: acf.prepareForAjax({
          action: 'acf/email_opt_in_banner/submit',
          email: email
        }),
        type: 'post',
        dataType: 'json'
      });
    }
    $input.on('input', clearError);
    function handleSubmit() {
      const email = ($input.val() || '').trim();
      if (email.length === 0) {
        showError(acf_email_opt_in_banner.empty_email);
        $input.trigger('focus');
        return;
      }
      if (!emailRegex.test(email) || !$input[0].checkValidity()) {
        showError(acf_email_opt_in_banner.invalid_email);
        $input.trigger('focus');
        return;
      }
      clearError();
      setSubmitting(true);
      submitOptIn(email).done(function (response) {
        if (!acf.isAjaxSuccess(response)) {
          setSubmitting(false);
          showError(acf_email_opt_in_banner.generic_error);
          $input.trigger('focus');
          return;
        }
        showSuccess();
      }).fail(function () {
        setSubmitting(false);
        showError(acf_email_opt_in_banner.generic_error);
        $input.trigger('focus');
      });
    }
    $submit.on('click', handleSubmit);

    // Banner lives inside the wp-admin posts-filter form; intercept Enter
    // so it doesn't submit the surrounding list-table filter form.
    $input.on('keydown', function (event) {
      if (event.key === 'Enter' || event.keyCode === 13) {
        event.preventDefault();
        handleSubmit();
      }
    });
    $dismiss.on('click', function () {
      $wrap.remove();
      persistState('dismissed');
    });
  });
})(jQuery);
/******/ })()
;
//# sourceMappingURL=acf-email-opt-in-banner.js.map
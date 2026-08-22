/**
 * Effect Studio — اسکریپت اصلی قالب
 * مدیریت منوی موبایل.
 */
( function () {
	'use strict';

	var toggle = document.querySelector( '.menu-toggle' );
	var mobileNav = document.getElementById( 'mobile-nav' );

	if ( toggle && mobileNav ) {
		toggle.addEventListener( 'click', function () {
			var isOpen = mobileNav.classList.toggle( 'is-open' );
			toggle.setAttribute( 'aria-expanded', isOpen ? 'true' : 'false' );
		} );
	}
} )();

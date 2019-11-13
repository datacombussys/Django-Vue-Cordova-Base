<template>
  <f7-page name="home">
    <!-- Top Navbar -->
    <f7-navbar title="Databoxx" :sliding="false">
      <f7-nav-left>
        <f7-link icon-ios="f7:menu" icon-aurora="f7:menu" icon-md="material:menu" panel-open="left"></f7-link>
      </f7-nav-left>

      <f7-nav-right>
        <f7-link
          icon-ios="f7:menu"
          icon-aurora="f7:menu"
          icon-md="material:menu"
          panel-open="right"
        ></f7-link>
      </f7-nav-right>
    </f7-navbar>

    <f7-subnavbar>
      <f7-button tab-link="#tab2" icon-f7="gear"></f7-button>
      <f7-button tab-link="#tab3" icon-f7="house"></f7-button>
      <f7-button tab-link="#tab1" icon-f7="lock"></f7-button>
      <f7-button tab-link="#tab 4" icon-f7="person"></f7-button>
    </f7-subnavbar>

    <!-- Page content-->

    <p>Grid cells have different size on Phone/Tablet</p>

    <f7-row>
      <!--- Left Column --->
      <f7-col width="100" medium="50">
        <f7-block>
          <f7-button fill raised popup-open="#my-popup">Popup</f7-button>
        </f7-block>
        <f7-block>
          <f7-button fill raised panel-open="left">Left Panel</f7-button>
        </f7-block>
      </f7-col>

      <!--- Right Column --->
      <f7-col width="100" medium="50">
        <f7-block>
          <f7-button fill raised login-screen-open="#my-login-screen">Login Screen</f7-button>
        </f7-block>
        <f7-block>
          <f7-button fill raised panel-open="right">Right Panel</f7-button>
        </f7-block>
      </f7-col>
    </f7-row>

    <f7-block-title medium>Block with Special (inset) Formatting</f7-block-title>
    <f7-block strong inset>
      <p>Donec et nulla auctor massa pharetra adipiscing ut sit amet sem. Suspendisse molestie velit vitae mattis tincidunt. Ut sit amet quam mollis, vulputate turpis vel, sagittis felis.</p>
    </f7-block>

    <!-- Toolbar-->
    <f7-toolbar class="footer-toolbar" bottom>
      <f7-link>Left Link</f7-link>
      <f7-link>Right Link</f7-link>
    </f7-toolbar>
  </f7-page>
</template>
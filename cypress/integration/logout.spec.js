import faker from 'faker';

const email = faker.internet.email();
const password = faker.internet.password();

describe('Logout', () => {
  it('should let a user logout', () => {
    // register user
    cy.visit('/register')
      .get('input[name="email"]')
      .type(email)

      .get('input[name="password"]')
      .type(password)

      .get('button[type="submit"]')
      .click();

    // log a user out
    cy.get('a')
      .contains('Log Out')
      .click();

    // assert "/logout" is displayed properly
    cy.get('p').contains('You are now logged out');

    cy.get('.navbar-collapse').within(() => {
      cy.get('.nav-link')
        .contains('User Status')
        .should('not.be.visible')

        .get('.nav-link')
        .contains('Log Out')
        .should('not.be.visible')

        .get('.nav-link')
        .contains('Log In')

        .get('.nav-link')
        .contains('Register');
    });
  });
});

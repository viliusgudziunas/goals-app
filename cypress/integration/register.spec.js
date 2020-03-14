import faker from 'faker';

const email = faker.internet.email();
const password = faker.internet.password();

describe('Register', () => {
  it('should display the registration form', () => {
    cy.visit('/register')
      .get('h1')
      .contains('Register')

      .get('form');
  });

  it('should allow a user to register', () => {
    // register user
    cy.visit('/register')
      .get('input[name="email"]')
      .type(email)

      .get('input[name="password"]')
      .type(password)

      .get('button[type="submit"]')
      .click();

    // assert user is redirected to "/"
    // assert "/" is displayed properly
    cy.get('h1').contains('All Users');

    cy.contains(email);

    cy.get('.navbar-collapse').within(() => {
      cy.get('.nav-link')
        .contains('User Status')

        .get('.nav-link')
        .contains('Log Out')

        .get('.nav-link')
        .contains('Log In')
        .should('not.be.visible')

        .get('.nav-link')
        .contains('Register')
        .should('not.be.visible');
    });
  });
});

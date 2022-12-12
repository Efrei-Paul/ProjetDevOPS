describe('Dashboard', () => {
  it('Checks if everything exist and work correctly', () => {
    cy.visit('http://0.0.0.0:8501')

    // Check that the title and the input exist
    cy.get('[id="prediction-de-prix-de-maison"]').should('exist')
    cy.get('[data-baseweb="input"]').should('exist')

    // Check the value of the input and click on the plus button
    cy.get('[data-baseweb="input"]')
      .invoke('val')
      .then((n) => {
    cy.get('.step-up').click({multiple: true })

    // Check that the incremented value is correct
    cy.get('input').should('have.value', String(n + 0.01))
  })

  })
})

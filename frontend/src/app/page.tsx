'use client';

import { useState } from 'react';
import { Box, Button, Input, VStack, Heading } from '@chakra-ui/react';
import { useRouter } from 'next/navigation';

export default function Home() {
  const [applianceType, setApplianceType] = useState('');
  const [budget, setBudget] = useState('');
  const router = useRouter();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    router.push(`/products?type=${applianceType}&budget=${budget}`);
  };

  return (
    <Box maxWidth="400px" margin="auto" mt={8}>
      <Heading as="h1" size="xl" textAlign="center" mb={6}>
        Appliance Search
      </Heading>
      <form onSubmit={handleSubmit}>
        <VStack spacing={4}>
          <Input
            placeholder="Appliance Type"
            value={applianceType}
            onChange={(e) => setApplianceType(e.target.value)}
          />
          <Input
            placeholder="Budget"
            type="number"
            value={budget}
            onChange={(e) => setBudget(e.target.value)}
          />
          <Button type="submit" colorScheme="blue" width="100%">
            Search Products
          </Button>
        </VStack>
      </form>
    </Box>
  );
}